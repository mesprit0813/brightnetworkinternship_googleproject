"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

def get_tags(tag_list):
    
    # this function gets tags from tuple
    
    temp_str =""
        
    if len(tag_list) >0:
                
        for j in range(len(tag_list)):
            temp_str += tag_list[j] +" "
                
        temp_str = temp_str.rstrip()
    
    return temp_str
    

def format_video(temp_video):
    
    # this function generates a string that contains all the information of a given video
    
    if type(temp_video) == list:
        
        tags_str = get_tags(temp_video[2])
                   
        return f"{temp_video[0]} ({temp_video[1]}) [{tags_str}]"
        
    else:
        
        tags_str = get_tags(temp_video.tags)        
                    
        return f"{temp_video.title} ({temp_video.video_id}) [{tags_str}]"
        

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        
        # define a variable for the current playing video
        self._current_playing = None
        # define the status of the current playing video, True - paused, False - not paused
        self._current_status = False
        # use a dict to store all the playlist by the lower version of their name
        self._all_playlist = {}
        # use a dict to store the video_id of the flagged videos and the reasons of flagging
        self._flag_list = {}
        
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        #print("show_all_videos needs implementation")
        # get all the videos from the library
        temp_videos = self._video_library.get_all_videos()
        
        
        #sort the videos in lexicographical order by title
        all_videos = []
        
        # transfer the video object into a list of object that contains all the information
        for i in range(len(temp_videos)):
            all_videos.append([temp_videos[i].title,temp_videos[i].video_id,
                               temp_videos[i].tags])
            
        # sort the videos by their titles
        all_videos.sort(key = lambda video:video[0])
                  
        # print the results
        print("Here's a list of all available videos:")
                
        for i in range(len(all_videos)):
            temp_str = "  "+format_video(all_videos[i]) # get the formatted result for each video
            
            # if the video has been flagged, show the flagged status and the reason
            if all_videos[i][1] in list(self._flag_list.keys()):
                temp_str += f" - FLAGGED (reason: {self._flag_list[all_videos[i][1]]})"
            
            print(temp_str)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        #print("play_video needs implementation")
        
        # get the required video by its video_id
        req_video = self._video_library.get_video(video_id)
        
        if req_video is None:
            # if the video does not exist
            print("Cannot play video: Video does not exist")
        elif video_id in list(self._flag_list.keys()):
            # if the video has been flagged
            print(f"Cannot play video: Video is currently flagged (reason: {self._flag_list[video_id]})")
        else:
            
            if self._current_playing is None: 
                # add the new video as the current playing one
                self._current_playing = req_video  
                self._current_status = False
                print(f"Playing video: {req_video.title}")
                
            else: 
                # replace the new video as the current playing one
                print(f"Stopping video: {self._current_playing.title}")
                self._current_playing = req_video
                self._current_status = False                
                print(f"Playing video: {req_video.title}")
                

    def stop_video(self):
        """Stops the current video."""

        #print("stop_video needs implementation")
        
        if self._current_playing is None:            
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._current_playing.title}")
            # update the related status
            self._current_playing = None
            self._current_status = False

    def play_random_video(self):
        """Plays a random video from the video library."""

        #print("play_random_video needs implementation")
        
        # get all the videos that haven't been flagged from the library        
        temp_videos = self._video_library.get_all_videos()            
        all_videos = [video for video in temp_videos if video.video_id not in list(self._flag_list.keys())]

               
        if len(all_videos) >0:
            random_video = random.choice(all_videos) # randomly pick one from the available list
        
            self.play_video(random_video.video_id)
        else: 
            print("No videos available")
        
    def pause_video(self):
        """Pauses the current video."""

        #print("pause_video needs implementation")
        if self._current_playing is None:
            # no video to pause
            print("Cannot pause video: No video is currently playing")
        else:
            if self._current_status:
                # the video has been paused
                print(f"Video already paused: {self._current_playing.title}")
            else:
                # pause the video if it hasn't been paused yet
                print(f"Pausing video: {self._current_playing.title}")
                self._current_status = True
            

    def continue_video(self):
        """Resumes playing the current video."""

        #print("continue_video needs implementation")
        
        if self._current_status: # if the video has been paused
            print(f"Continuing video: {self._current_playing.title}")
            self._current_status = False
        elif self._current_playing is None: # if there is no video being played
            print("Cannot continue video: No video is currently playing")
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""

        #print("show_playing needs implementation")
        
        if self._current_playing is None:
            print("No video is currently playing")
        else:
            # add title and video_id
            temp_text = format_video(self._current_playing)
            
            if self._current_status:
                temp_text += " - PAUSED"
        
            print("Currently playing: "+temp_text)
            

    # playlist and etc
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("create_playlist needs implementation")
        
        if playlist_name.lower() in list(self._all_playlist.keys()): # if the playlist has been created already
            print("Cannot create playlist: A playlist with the same name already exists")
        else:        
            self._all_playlist[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {playlist_name}")
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        #print("add_to_playlist needs implementation")
        temp_error = f"Cannot add video to {playlist_name}: "
        
        # get the video from the library first
        req_video = self._video_library.get_video(video_id)
        
        
        if playlist_name.lower() not in list(self._all_playlist.keys()): # if the playlist doesn't exist yet
            print(temp_error+"Playlist does not exist")
        elif req_video is None:
            print(temp_error+"Video does not exist")
        elif video_id in list(self._flag_list.keys()):
            # if the video has been flagged
            print(temp_error+f"Video is currently flagged (reason: {self._flag_list[video_id]})")
        
        else:
            temp_res = self._all_playlist[playlist_name.lower()].add_video(video_id,req_video)
            
            if not temp_res:
                print(temp_error+"Video already added")
            else:
                print(f"Added video to {playlist_name}: {req_video.title}")
        

    def show_all_playlists(self):
        """Display all playlists."""

        #print("show_all_playlists needs implementation")
        
        if len(self._all_playlist) ==0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            temp_pll = list(self._all_playlist.values())
            pl_name = []
            for i in range(len(temp_pll)):
                pl_name.append(temp_pll[i].name())
            
            pl_name.sort()
            for name in pl_name:
                print("  "+ name)
            
            

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("show_playlist needs implementation")
        
        if playlist_name.lower() not in list(self._all_playlist.keys()):
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            
        else:
            print(f"Showing playlist: {playlist_name}")
        
            temp_pl = self._all_playlist[playlist_name.lower()]
        
            temp_content = temp_pl.get_videos()
        
            if len(temp_content) ==0 :
                print("  No videos here yet")
            else:
                for temp_video in temp_content:
                    
                    temp_str = "  "+format_video(temp_video)
                    
                    if temp_video.video_id in list(self._flag_list.keys()):
                        
                        temp_str += f" - FLAGGED (reason: {self._flag_list[temp_video.video_id]})"
                    
                    print(temp_str)
        

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        #print("remove_from_playlist needs implementation")
        
        req_video = self._video_library.get_video(video_id)
        temp_error = f"Cannot remove video from {playlist_name}: "
        
        if req_video is None:
            print(temp_error +"Video does not exist")
        elif playlist_name.lower() not in list(self._all_playlist.keys()):
            print(temp_error+"Playlist does not exist")
        else:
            
            temp_res = self._all_playlist[playlist_name.lower()].remove_video(video_id) 
                        
            if temp_res is not None:
                print(f"Removed video from {playlist_name}: {req_video.title}")
            else:
                print(temp_error+"Video is not in playlist")  
            

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("clears_playlist needs implementation")
        if playlist_name.lower() not in list(self._all_playlist.keys()):
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self._all_playlist[playlist_name.lower()].clear_playlist()
            print(f"Successfully removed all videos from {playlist_name}")
            

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        #print("deletes_playlist needs implementation")
        temp_pl = self._all_playlist.pop(playlist_name.lower(),None)
        if temp_pl is None:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Deleted playlist: {playlist_name}")

    ############################################################
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        #print("search_videos needs implementation")
        
        # get all the titles 
        
        temp_videos = self._video_library.get_all_videos()
            
        all_videos = [video for video in temp_videos if video.video_id not in list(self._flag_list.keys())]
            
        temp_result = []
        
        for video in all_videos:
            
            temp_title = video.title.lower()
            
            if temp_title.find(search_term.lower()) > -1:
                temp_result.append([video,video.title])
            
        if len(temp_result) >0:
            temp_result.sort(key = lambda video:video[1])
            print(f"Here are the results for {search_term}:")
            
            
            result_index = list(range(1,len(temp_result)+1))
            
            for i in result_index:
                print(f"  {i}) {format_video(temp_result[i-1][0])}")
            
            
            ## ask people if they want to play any search result. 
            print("""Would you like to play any of the above? If yes, specify the number of the video. 
            If your answer is not a valid number, we will assume it's a no.""")
            
        
            number = input()
            
            str_rind = [str(ind) for ind in result_index]
                      
            if str(number) in str_rind:
                
                self.play_video(temp_result[int(number)-1][0].video_id)
            else:
                pass
                
        else:
            print(f"No search results for {search_term}")
        
        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        #print("search_videos_tag needs implementation")
        temp_videos = self._video_library.get_all_videos()
            
        all_videos = [video for video in temp_videos if video.video_id not in list(self._flag_list.keys())]
            
        temp_result = []
        
        for video in all_videos:
            
            if video_tag.lower() in video.tags:
                temp_result.append([video,video.title])
        
        if len(temp_result) >0:
            temp_result.sort(key = lambda video:video[1])
            print(f"Here are the results for {video_tag}:")
            
            
            result_index = list(range(1,len(temp_result)+1))
            
            for i in result_index:
                print(f"  {i}) {format_video(temp_result[i-1][0])}")
            
            
            ## ask people if they want to play any search result. 
            print("""Would you like to play any of the above? If yes, specify the number of the video. 
            If your answer is not a valid number, we will assume it's a no.""")
            
        
            number = input()
            str_rind = [str(ind) for ind in result_index]
                      
            if str(number) in str_rind:
                
                self.play_video(temp_result[int(number)-1][0].video_id)
            else:
                pass
                
        else:
            print(f"No search results for {video_tag}")
        
    
    ##########################################################################
    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        #print("flag_video needs implementation")
                
        temp_error = "Cannot flag video: "
        
        req_video = self._video_library.get_video(video_id)
                
        if req_video is None:
            print(temp_error + "Video does not exist")
        elif video_id in list(self._flag_list.keys()):
            print(temp_error + "Video is already flagged")
        else:
            self._flag_list[video_id] = flag_reason
            
            if self._current_playing is None:
                pass
            elif self._current_playing.video_id == video_id:
                self.stop_video()
            
            print(f"Successfully flagged video: {req_video.title} (reason: {flag_reason})")
            

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        #print("allow_video needs implementation")
        temp_error = "Cannot remove flag from video: "
        
        if self._video_library.get_video(video_id) is None:
            print(temp_error +"Video does not exist")
        
        else:
            temp_pop = self._flag_list.pop(video_id, None)
            if temp_pop is None:
                print(temp_error +"Video is not flagged")
            else:
                print(f"Successfully removed flag from video: {self._video_library.get_video(video_id).title}")
