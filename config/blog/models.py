from django.db import models
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    
    title = models.CharField(max_length = 200, unique = True)
    
    author = models.ForeignKey(
        'auth.User', 
        on_delete = models.CASCADE,
    )
    
    # slug = models.SlugField(max_length = 50, unique = True)

    body = models.TextField()

    
    
    pub_date = models.DateField(
        'date published',
        auto_now_add = True

    )

    updated_on = models.DateTimeField(auto_now = True)

    status = models.IntegerField(choices = STATUS, default = 0)


    class Meta:
        ordering = ['-pub_date']


    def __str__(self):
        return "{} on [{}]".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d')
        )



    def get_absolute_url(self):
        return reverse('post_detail',args = [str(self.id)])


