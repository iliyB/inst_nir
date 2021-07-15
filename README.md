# inst_nir

Use: https://github.com/adw0rd/instagrapi
Use: https://imageai.readthedocs.io/en/latest/

For use video_download_from_story add a new method in "instagrapi/mixins/video.py" 

    def video_download_from_story(self, story_pk: int, folder: Path = "") -> Path:
        """
        Download video using story pk
        """
        
        story = self.story_info(story_pk)
        assert story.media_type == 2, "Must been video"
        filename = "{username}_{story_pk}".format(
            username=story.user.username, story_pk=story_pk
        )
        return self.video_download_by_url(story.video_url, filename, folder)
    
For use photo_download_from_story add a new method in "instagrapi/mixins/photo.py" 

        def photo_download_from_story(self, story_pk: int, folder: Path = "") -> Path:
        """
        Download photo using story pk
        """
        
        story = self.story_info(story_pk)
        assert story.media_type == 1, "Must been photo"
        filename = "{username}_{story_pk}".format(
            username=story.user.username, story_pk=story_pk
        )
        return self.photo_download_by_url(story.thumbnail_url, filename, folder)
      
Add class login with fields: Login and Passwords
Add database with format <name>.xml

