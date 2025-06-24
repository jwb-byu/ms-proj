import numpy

# import random
from typing import Tuple

# from brainbox.io.one import EphysSessionLoader, SessionLoader, SpikeSortingLoader # type: ignore
from brainbox.io.spikeglx import Streamer  # type: ignore
from ibldsp.voltage import destripe, destripe_lfp  # type: ignore

# from mtscomp import decompress # type: ignore
from one.api import OneAlyx, ONE  # type: ignore


class OneHandler:
    def __init__(self) -> None:
        """
        A helper class to abstract away use of IBL's ONE-api
        """
        self.one: OneAlyx = ONE(
            cache_dir="/Users/wesley/GitHub/BYU/ms-proj/tmp/one-cache",
            base_url="https://openalyx.internationalbrainlab.org",
            password="international",
            silent=True,
        )  # type: ignore

        self.data_tag = "2024_Q2_IBL_et_al_BWM_iblsort"  # tag for most recent data release (https://figshare.com/articles/preprint/Data_release_-_Brainwide_map_-_Q4_2022/21400815?file=49286065)
        self.all_sessions = self.one.search(tag=self.data_tag, query_type="remote")
        self.n_sessions = len(self.all_sessions)  # type: ignore
        self.all_insertions = self.one.search_insertions(
            tag=self.data_tag, query_type="remote"
        )
        self.n_insertions = len(self.all_insertions)  # type: ignore

        return None

    def get_r_ins(self) -> Tuple[str, str, str]:
        """
        Get a random insertion and return its corresponding insertion and session IDs

        :return: (insertion/probe id, insertion/probe name, session/experiment id)
        """
        # i = random.randint(0, (self.n_insertions-1))
        # pid = str(self.all_insertions[i]) # type: ignore
        pid = "695476f6-4c14-4a2f-b658-948514629079"  # TODO: remove later
        eid, p_name = self.one.pid2eid(pid)

        return pid, str(p_name), str(eid)

if __name__ == "__main__":
    one_handler = OneHandler()
    pid, p_name, eid = one_handler.get_r_ins()

    loaded_dta: dict = {}
    for dta in one_handler.one.list_datasets(
        eid, collection=f"raw_ephys_data/{p_name}"
    ):
        loaded_dta[str(dta)] = one_handler.one.load_dataset(eid, dataset=str(dta))

    loaded_types = {k: type(v) for k, v in loaded_dta.items()}
    loaded_shapes = {
        k: (v.shape if type(v) is numpy.ndarray else type(v))
        for k, v in loaded_dta.items()
    }

    # ??? decompressed_raw_reader = decompress(loaded_dta['raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.cbin'], loaded_dta['raw_ephys_data/_spikeglx_ephysData_g0_t0.nidq.ch'])
    ap_streamer = Streamer(
        pid=pid, one=one_handler.one, remove_cached=False, typ="ap"
    )  # I think these are the source of truth for raw data
    lf_streamer = Streamer(
        pid=pid, one=one_handler.one, remove_cached=False, typ="lf"
    )  # I think these are the source of truth for raw data

    # Destripe the ap signal
    destriped_ap = destripe(ap_streamer[0:-1, 0:-1].T, fs=ap_streamer.fs)  # type: ignore
    destriped_lf = destripe_lfp(lf_streamer[0:-1, 0:-1].T, fs=lf_streamer.fs)  # type: ignore

    raise NotImplementedError("Break")


# ONE-api/ibllib Details:
# - Demo: https://colab.research.google.com/drive/1y3sRI1wC7qbWqN6skvulzPOp6xw8tLm7

# - PyPi: https://pypi.org/project/ONE-api/
# - Docs: https://int-brain-lab.github.io/ONE/
# - Repo: https://github.com/int-brain-lab/ONE

# - PyPi: https://pypi.org/project/ibllib/
# - Docs: https://int-brain-lab.github.io/iblenv/
# - Repo: https://github.com/int-brain-lab/ibllib

# from brainbox.io.one import EphysSessionLoader, SessionLoader, SpikeSortingLoader
# from brainbox.io.spikeglx import Streamer
# from one.api import OneAlyx, ONE

# """OneAlyx"""
# one: OneAlyx = ONE(
#     cache_dir='/Users/wesley/GitHub/BYU/ms-proj/tmp/one-cache',
#     base_url="https://openalyx.internationalbrainlab.org",
#     password="international",
#     silent=True
# ) # type: ignore

# """Search"""
# one.search() # search on sessions
# one.search_terms("remote") # properties for session searching
# one.search_insertions() # search on insertions
# one.search_terms("remote", "insertions") # properties for insertion searching
# tag="2024_Q2_IBL_et_al_BWM_iblsort" # tag for most recent data release (https://figshare.com/articles/preprint/Data_release_-_Brainwide_map_-_Q4_2022/21400815?file=49286065)
# insertions = one.search_insertions(tag="2024_Q2_IBL_et_al_BWM_iblsort", query_type="remote") # search by tag
# sessions = one.search(tag=tag, query_type="remote") # search by tag

# """EID, PID"""
# eid = sessions[0] # type: ignore
# pid = insertions[0] # type: ignore
# pids, labels = one.eid2pid(eid) # conversion
# eid, pname = one.pid2eid(pid) # conversion

# """Collections, Datasets"""
# datasets = one.list_datasets(eid) # list datasets # also `one.list_datasets(eid, collection='foo.bar')`
# one.describe_dataset("foo.bar") # prints and returns a description
# collections = one.list_collections(eid) # list collections
# data_sets = one.list_datasets(collection="raw_ephys_data", eid=eid)
# raw_ephys_data_collection_name = 'raw_ephys_data'
# x = one.load_dataset(eid, dataset='foo.bar') # load data

# """SessionLoader"""
# sess_loader = SessionLoader(one=one, eid=eid) # instantiate a session loader
# sess_loader.load_trials() # Load in trials data
# sess_loader.load_wheel() # Load in wheel data
# sess_loader.load_pose(views=["left", "right"]) # Load in pose data
# sess_loader.load_motion_energy(views=["left", "right"]) # Load in motion energy
# sess_loader.load_pupil() # Load in pupil diameter
# sess_loader.load_session_data() # do all of the above
# sess_loader.trials # access trials
# sess_loader.wheel # access another table, etc.

# """SpikeSortingLoader"""
# spike_loader = SpikeSortingLoader(pid=pid, one=one)  # instantiate with a pid
# spike_loader = SpikeSortingLoader(eid=eid, one=one, pname=pname) # alternatively instantiate with an eid and probe name
# spikes, clusters, channels = spike_loader.load_spike_sorting() # download and load data
# clusters = spike_loader.merge_clusters(spikes, clusters, channels) # Assign brain location information from channels to clusters

# """EphysSessionLoader"""
# ephys_sess_loader = EphysSessionLoader(eid=eid, one=one) # instantiate with an eid
# ephys_sess_loader.load_session_data() # load session data
# ephys_sess_loader.load_spike_sorting() # load spike data
# ephys_sess_loader.trials # access trials
# ephys_sess_loader.wheel # access another table, etc.

# """Ephys Streamer"""
# time0 = 100  # timepoint in recording to stream
# time_win = 1  # number of seconds to stream
# ephys_stream = Streamer(pid=pid, one=one, remove_cached=False, typ="ap") # instantiate the streamer, typ=["ap"|"lf"]
# s0 = time0 * ephys_stream.fs # index considering sampling frequency
# tsel = slice(int(s0), int(s0) + int(time_win * ephys_stream.fs)) # slice only a subset
# raw = ephys_stream[tsel, : -ephys_stream.nsync].T # Important: remove sync channel from raw data, and transpose
