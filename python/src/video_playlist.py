"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    
    def __init__(self,name):
        self._name = name
        self._value = {}
    
    def name(self):
        return self._name
    
    def get_videos(self):
        return list(self._value.values())
    
    def get_video_id(self):
        return list(self._value.keys())
    
    def check_video(self,video_id):
        
        if video_id in self.get_video_id():
            return True
        else:
            return False    
    
    def add_video(self,video_id,video):
        
        if self.check_video(video_id):
            return False
        else:
            self._value[video_id] = video
            return True
        
    def remove_video(self,video_id):
        return self._value.pop(video_id, None)
        
    def clear_playlist(self):
        self._value = {}
        
        
        

            
