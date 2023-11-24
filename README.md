# IISc_Capstone_TimeGAN_CNN
This implementation of Time-series Generative Adversarial Networks (TimeGAN)is inspired by the original work of Jinsung Yoon, Daniel Jarrett, and Mihaela van der Schaar. 

This implementation is done using TimeGAN with CNNs as the Embedder, Recovery, Supervisor and Discriminator Networks, 
In this implementation, One audio file was used and trained the Audio files were converted to STFT and then passed on through the Network

And it was observed that the Generator->Supervisor->Recovery Network when train could successfully reproduce the audio with which it was train when a normally 
distributed random data was provided to it as input.. 

