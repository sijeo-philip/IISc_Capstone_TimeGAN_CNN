# IISc_Capstone_TimeGAN_CNN
Time-series Generative Adversarial Networks (TimeGAN) is the work of Jinsung Yoon, Daniel Jarrett, and Mihaela van der Schaar (paper). 
This repository implements TimeGAN (original code) with TensorFlow 2.X version, mainly for the Hide-and-seek privacy challenge held by NeurIPS (webpage).

This implementation is done using TimeGAN with CNNs as the Embedder, Recovery, Supervisor and Discriminator Networks, 
In this implementation, One audio file was used and trained the Audio files were converted to STFT and then passed on through the Network

And it was observed that the Generator->Supervisor->Recovery Network when train could successfully reproduce the audio with which it was train when a normally 
distributed random data was provided to it as input.. 

