from django.db import models

# Create your models here.


class videos_collection(models.Model):
    Video_name = models.CharField(max_length=255,null=True, blank=True)
    Release_Date = models.DateTimeField(null=True,blank=True)
    Poster_Image_uri = models.URLField(null=True,blank=True)
    Likes = models.IntegerField(null=True,blank=True)
    Disclike = models.IntegerField(null=True,blank=True)
    Url = models.TextField(null=True,blank=True)
    Title = models.CharField(max_length=255)
    Discription = models.TextField(null=True,blank=True)
    Pornstarts = models.CharField(max_length=500,null=True,blank=True)
    Category = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self) -> str:
        video_title = ""
        video_name_li = self.Video_name.split('_')
        if video_name_li[0] == 'scene' :
            try: 
                int(video_name_li[1])
                video_title += 'brazzers_'
            except : ...
        elif video_name_li[0] != 'scene' :
            try: 
                video_title += self.Category
            except : ...
        if 'videos_' in self.Video_name:
            video_name = self.Video_name.replace('videos_','')
            video_title += video_name
        else:
            video_title += self.Video_name
        return video_title
    
class configuration(models.Model):
    website_name = models.CharField(max_length=255,null=True,blank=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    category = models.CharField(max_length=255,null=True,blank=True)
    more_than_old_days_download = models.IntegerField(null=True,blank=True)
    numbers_of_download_videos = models.IntegerField(null=True,blank=True)
    delete_old_days = models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.website_name
