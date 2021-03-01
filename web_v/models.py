from django.db import models

# Create your models here.

class lost_find_topic(models.Model):
    text = models.CharField(max_length=300)
    L_F_T_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class lost_find_entry(models.Model):
    L_F_T = models.ForeignKey(lost_find_topic, on_delete=models.CASCADE)
    text = models.TextField()
    L_F_T_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Lost_find_topic_entries'

    def __str__(self):
        return self.text[:50] + "..."

class electronics_topic(models.Model):
    text = models.CharField(max_length=300)
    E_T_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class electronics_entry(models.Model):
    E_T = models.ForeignKey(electronics_topic, on_delete=models.CASCADE)
    text = models.TextField()
    E_T_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Electronics_topic_entries'

    def __str__(self):
        return self.text[:50] + "..."

class necessary_topic(models.Model):
    text = models.CharField(max_length=300)
    N_T_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class necessary_entry(models.Model):
    N_T = models.ForeignKey(necessary_topic, on_delete=models.CASCADE)
    text = models.TextField()
    N_T_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Necessary_topic_entries'

    def __str__(self):
        return self.text[:50] + "..."
