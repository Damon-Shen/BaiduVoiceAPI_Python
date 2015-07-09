#coding:utf-8
# 录制语音API 配合Baidu语音识别API使用
#-------------------------------------------------
# Ver 0.2.1
# 修复在树莓派下无法录音的问题
#-------------------------------------------------
# Ver 0.2
# 修复了一个变量未声明导致的程序错误 
#-------------------------------------------------
# Ver 0.1
# 本API只是调用了Pyaudio开源lib
# windows下载地址(x86 Only):http://people.csail.mit.edu/hubert/pyaudio/
# Raspberry Pi下载方式: sudo apt-get install python-pyaudio             
#                                  
#-------------------------------------------------
# Create By Damon.shen


import pyaudio
import wave

def RecordSub(Channels, Rate, Chunk, Input_device, Record_seconds, FileName):
        try:   
                p = pyaudio.PyAudio()

                stream = p.open(format = pyaudio.paInt16,
                        channels = Channels,
                        rate = Rate,
                        input_device = Input_device
                        input = True,
                        frames_per_buffer = Chunk)

                frames = []

                for i in range(0, int(Rate / Chunk * Record_seconds)):
                    data = stream.read(Chunk)
                    frames.append(data)

                stream.stop_stream()
                stream.close()
                p.terminate()

                wf = wave.open(FileName, 'wb')
                wf.setnchannels(Channels)
                wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(Rate)
                wf.writeframes(b''.join(frames))
                wf.close()

                return 'done'
        except Exception, e:
                return e; 

    
            
        
