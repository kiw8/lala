#왜 Fmax*2를 해야하는지 확인
import numpy as np
import matplotlib.pyplot as plt

#원본 신호 파라미터
f_max = 5 #최대주파수(Hz)
t =np.linspace(0,1,1000,endpoint=False) #1초 동안의 시간 벡터

#원본 신호 생성
continuous_signal = np.sin(2*np.pi*f_max*t)

#그래프 생성
plt.figure(figsize=(12,9))
for i,fs in enumerate(sampling_frequencies):
    #샘플링 간격
    sample_interval = int(1000/fs)
    sampled_t = t[::sample_interval]
    sampled_signal = continuous_signal[::sample_interval]

    #플롯
    plt.subplot(len(sampling_frequencies),1,i+1)
    plt.stem(sampled_t, sampled_signal, 'r', markerfmt='ro', basefmt="", linefmt='r-', label='Sampled Signal')
    plt.title(f'Sampling Frequencies = {fs}Hz (Nyquist Frequency = {2*f_max}Hz)')
    plt.xlabel('Time[s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

