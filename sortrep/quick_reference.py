# from brainbox.io.one import EphysSessionLoader, SessionLoader, SpikeSortingLoader
# from brainbox.io.spikeglx import Streamer
# from one.api import OneAlyx, ONE


"""OneAlyx"""
# one: OneAlyx = ONE(
#     cache_dir='/Users/wesley/GitHub/BYU/ms-proj/tmp/one-cache',
#     base_url="https://openalyx.internationalbrainlab.org",
#     password="international",
#     silent=True
# ) # type: ignore

"""Search"""
# one.search() # search on sessions
# one.search_terms("remote") # properties for session searching
# one.search_insertions() # search on insertions
# one.search_terms("remote", "insertions") # properties for insertion searching
# tag="2024_Q2_IBL_et_al_BWM_iblsort" # tag for most recent data release (https://figshare.com/articles/preprint/Data_release_-_Brainwide_map_-_Q4_2022/21400815?file=49286065)
# insertions = one.search_insertions(tag="2024_Q2_IBL_et_al_BWM_iblsort", query_type="remote") # search by tag
# sessions = one.search(tag=tag, query_type="remote") # search by tag


"""EID, PID"""
# eid = sessions[0] # type: ignore
# pid = insertions[0] # type: ignore
# pids, labels = one.eid2pid(eid) # conversion
# eid, pname = one.pid2eid(pid) # conversion


"""Collections, Datasets"""
# datasets = one.list_datasets(eid) # list datasets # also `one.list_datasets(eid, collection='foo.bar')`
# one.describe_dataset("foo.bar") # prints and returns a description
# collections = one.list_collections(eid) # list collections
# data_sets = one.list_datasets(collection="raw_ephys_data", eid=eid)
# raw_ephys_data_collection_name = 'raw_ephys_data'
# x = one.load_dataset(eid, dataset='foo.bar') # load data


"""SessionLoader"""
# sess_loader = SessionLoader(one=one, eid=eid) # instatiate a session loader
# sess_loader.load_trials() # Load in trials data
# sess_loader.load_wheel() # Load in wheel data
# sess_loader.load_pose(views=["left", "right"]) # Load in pose data
# sess_loader.load_motion_energy(views=["left", "right"]) # Load in motion energy
# sess_loader.load_pupil() # Load in pupil diameter
# sess_loader.load_session_data() # do all of the above
# sess_loader.trials # access trials
# sess_loader.wheel # access another table, etc.


"""SpikeSortingLoader"""
# spike_loader = SpikeSortingLoader(pid=pid, one=one)  # instantiate with a pid
# spike_loader = SpikeSortingLoader(eid=eid, one=one, pname=pname) # alternatively instantiate with an eid and probe name
# spikes, clusters, channels = spike_loader.load_spike_sorting() # download and load data
# clusters = spike_loader.merge_clusters(spikes, clusters, channels) # Assign brain location information from channels to clusters


"""EphysSessionLoader"""
# ephys_sess_loader = EphysSessionLoader(eid=eid, one=one) # instantiate with an eid
# ephys_sess_loader.load_session_data() # load session data
# ephys_sess_loader.load_spike_sorting() # load spike data
# ephys_sess_loader.trials # access trials
# ephys_sess_loader.wheel # access another table, etc.


"""Ephys Streamer"""
# time0 = 100  # timepoint in recording to stream
# time_win = 1  # number of seconds to stream
# ephys_stream = Streamer(pid=pid, one=one, remove_cached=False, typ="ap") # instantiate the streamer, typ=["ap"|"lf"]
# s0 = time0 * ephys_stream.fs # index considering sampling frequency
# tsel = slice(int(s0), int(s0) + int(time_win * ephys_stream.fs)) # slice only a subset
# raw = ephys_stream[tsel, : -ephys_stream.nsync].T # Important: remove sync channel from raw data, and transpose
