# BaiduVoiceAPI_Python
百度语音API的Python版，目前仅支持语音解析

调用方法
VoiceTranslation =  BaiduVoiceTranslationAPI.BaiduVoiceHttpClient(apiKey,secretKey)
VoiceRespone = VoiceTranslation.VocieTranslation(Language,Channel,audioFile,Format,Rate)

print VoiceRespone
