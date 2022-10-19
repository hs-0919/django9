from django.db import models

# Create your models here.
# 카페에서 복사함, id를 설정하지 않으면 자동증가로 설정된다.
class BoardTab(models.Model):
    name = models.CharField(max_length = 20)
    passwd = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    cont = models.TextField()
    bip = models.GenericIPAddressField() # board ip 담는거
    bdate = models.DateTimeField()
    readcnt = models.IntegerField() # 조회수
    gnum = models.IntegerField() # 그룹넘버 - 원글에 id를 가짐
    onum = models.IntegerField() # 오더넘버 -보여주는 순서?
    nested = models.IntegerField() # 댓글의 들여쓰기 -댓글으 ㅣ댓글 수












