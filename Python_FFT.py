#The following code demonstrates a couple of examples of using a fast fourier transform on an input signal to
#determine its frequency content.  The first example looks at a sine wave with a single frequency, so the real
#component of the Fourier transform of the signal will show a peak at that frequency.  The second example looks at
#the frequency content of a square wave signal.





#Numeric Python library
import numpy as np


#Plotting library
from matplotlib import pyplot as plt


#Scientific library of special functions
from scipy import special






def FFT_Plot(t_ll, t_ul, samples, signal, f, time):




    #Create a figure to plot both the signal and its Fourier transform
    plt.figure()



    #First subplot showing the sine wave signal.
    plt.subplot(3,1,1)



    #Plot of the signal.  The horizontal axis is set to the time range defined previously.  The vertical axis
    #is set to the min(signal) - max(signal)/5 to max(signal) + max(signal)/5.
    plt.plot(time, signal)
    plt.xlim(t_ll,t_ul)
    plt.ylim((np.min(signal) - np.max(signal)/5), (np.max(signal) + np.max(signal)/5))



    #Label the axes.
    plt.xlabel('Time(s)')
    plt.ylabel('Signal amplitude (A.U.)')




    #The second subplot shows the Fourier transform  magnitude of the sine wave signal.
    plt.subplot(3,1,2)



    #Calculate the FFT of the sine wave signal.
    sp = np.fft.fft(signal)



    #Calculate the frequency axis for the FFT.  This is determined based on the number of time samples
    #and the frequency sampling period is determined with the ratio of the total time divided by the
    #total number of samples.
    freq = np.fft.fftfreq(samples, d = (t_ul - t_ll)/samples)



    #Perform an FFT shift on the frequencies and the transform itself.
    freq = np.fft.fftshift(freq)
    sp = np.fft.fftshift(sp)



    #Magnitude of the FFT.  This is what will be plotted.
    mag_sp = np.absolute(sp)



    #Plot the magnitude of the FFT of the signal.  Scale the frequency range to +/- 3 times the maximum signal
    #frequency.  The y axis will range from min(FTT) - Min(FFT)/5 to Max(FFT) + Max(FFT)/5.
    plt.plot(freq, mag_sp)
    plt.xlim(-3*f, 3*f)
    plt.ylim((np.min(mag_sp)-np.max(mag_sp)/5), (np.max(mag_sp) + np.max(mag_sp)/5))



    #Label the plot axes for the FFT of the signal.
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('FFT magnitude (A.U.)')




    #The final subplot shows the Fourier transform of the sine wave signal.
    plt.subplot(3,1,3)


    #Magnitude of the FFT.  This is what will be plotted.
    angle_sp = np.angle(sp)
    angle_sp = np.degrees(angle_sp)
    angle_sp = np.fft.fftshift(angle_sp)



    #Plot the real component of the FFT of the signal.  Set the frequency plot limits between 0 and 50 Hz.
    plt.plot(freq, angle_sp)
    plt.xlim(-3*f, 3*f)
    plt.ylim((np.min(angle_sp)+np.min(angle_sp)/5), (np.max(angle_sp) + np.max(angle_sp)/5))



    #Label the plot axes for the FFT of the signal.
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('FFT phase (Degrees)')



    #Show both the signal and FFT plots of the sine wave signal.
    plt.show()


    return





#EXAMPLE 1.
#First example of determining an FFT of a sine wave.


#Lower limit for time (seconds)
t_ll = 0



#Upper limit for time (seconds)
t_ul = 0.5



#Number of time samples for the signal in question to cover the full time range.  To satisfy Nyquist's
#theorem, the sampling frequency must be at least double the largest frequency in the input signal.
samples = 20000



#Create a horizontal axis as time, t.
time = np.linspace(t_ll,t_ul,samples)


#Frequency of the signal.
f = 30


#The first signal is a sine wave with frequency f = 30 Hz.
signal_sine = np.sin(2*np.pi*f*time)



#Use the FFT_Plot function to calculate and plot the FFT (magnitude and phase) for the sine wave.
FFT_Plot(t_ll, t_ul, samples, signal_sine, f, time)








#EXAMPLE 2.
#First example of determining an FFT of a Bessel function of order 3.


#Lower limit for time (seconds)
t_ll_b = 0



#Upper limit for time (seconds)
t_ul_b = 50



#Number of time samples for the signal in question to cover the full time range.  To satisfy Nyquist's
#theorem, the sampling frequency must be at least double the largest frequency in the input signal.
samples_b = 20000



#Create a horizontal axis as time, t.
time_b = np.linspace(t_ll_b,t_ul_b,samples_b)


#Frequency arguement for the x-axis plotting of the FFT.
f_b = 1


#Calculate Bessel function of the first kind of order 3
signal_Bessel = special.jn(3,time_b)



#Use the FFT_Plot function to calculate and plot the FFT (magnitude and phase) for the Bessel function.
FFT_Plot(t_ll_b, t_ul_b, samples_b, signal_Bessel, f_b, time_b)









