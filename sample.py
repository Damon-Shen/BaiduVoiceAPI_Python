#coding:utf-8

import BaiduVoiceTranslationAPI
import RecordAPI
import sys
 
apiKey = ""                             #这里输入自己的key
secretKey = ""                          #这里输入自己的secretKey
audioFile = sys.path[0] + '/Translation.wav'  				#生成并解析的语音路径+文件名 默认在当前程序所在目录
Language = "zh"                         			        #默认zh 支持中文(zh) 英文(en) 粤语(ct)                         					 		
Rate = 16000                          				        #采样率，支持8000和16000
Channel = 1                             			        #声道，目前baidu只支持单声道
Format = 'wav'                                              #语音格式，支持wav pcm opus speex amr x-flac
Chunk = 1024                                                #录音块长度
Record_secounds = 5                                         #录音时长，单位:秒


if (not apiKey or not secretKey):
    print 'Key Empty'
    sys.exit(0)
    
# 开始录音
Record = RecordAPI.RecordSub(Channel,Rate,Chunk,Record_secounds,audioFile)

#录音完成
if (Record == 'done'):
    # 开始语音解析
    VoiceTranslation =  BaiduVoiceTranslationAPI.BaiduVoiceHttpClient(apiKey,secretKey)

    VoiceRespone = VoiceTranslation.VocieTranslation(Language,Channel,audioFile,Format,Rate)
    # 输出解析结果
    print VoiceRespone
else:
    #录音失败，返回错误代码
    print Record


https://github.com/Damon-Shen/BaiduVoiceAPI_Python.git
