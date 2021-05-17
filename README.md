# inst_nir

Use: https://github.com/adw0rd/instagrapi

For use video_download_from_story add a new method in "instagrapi/mixins/video.py" 

    def video_download_from_story(self, story_pk: int, folder: Path = "") -> Path:
        """
        Download video using media pk

                Parameters
                ----------
                story_pk: int
                    Unique Story ID
                folder: Path, optional
                    Directory in which you want to download the album, default is "" and will download the files to working dir.

                Returns
                -------
                Path
                    Path for the file downloaded
        """
        story = self.story_info(story_pk)
        assert story.media_type == 2, "Must been video"
        filename = "{username}_{story_pk}".format(
            username=story.user.username, story_pk=story_pk
        )
        return self.video_download_by_url(story.video_url, filename, folder)
