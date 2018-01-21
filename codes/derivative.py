# -----------------------------------------------------------------------------------
# Title: Data Filtering
# Author: Nelson Ribeiro Filho
# Description: Source codes for potential field filtering
# Collaborator: Rodrigo Bijani
# -----------------------------------------------------------------------------------

# Import Python libraries
from __future__ import division
import warnings
import numpy as np
import auxiliars as aux

def xderiv(x, y, data, n):
    
    '''
    Return the horizontal derivative in x direction for n order in Fourier domain.
    
    Inputs:
    x - numpy 2D array - grid values in x direction
    y - numpy 2D array - grid values in y direction
    data - numpy 2D array - potential data
    n - float - order of the derivative
    
    Output:
    xder - numpy 2D array - derivative in x direction
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape != data.shape:
        raise ValueError("All inputs must have same shape!")

    # Condition for the order of the derivative
    assert n >= 0., 'Order of the derivative must be positive and nonzero!'
    
    if n == 0.:
        res = data
    else:    
        # Calculate the wavenuber in x direction
        kx, _ = aux.wavenumber(x,y)
        # Apply the Fourier transform
        xder = np.fft.fft2(data)*((kx*1j)**(n))
        # Calculating the inverse transform
        res = np.real(np.fft.ifft2(xder))
    
    # Return the final output
    return res

def yderiv(x, y, data, n):
    
    '''
    Return the horizontal derivative in y direction for n order in Fourier domain.

    Inputs:
    x - numpy 2D array - grid values in x direction
    y - numpy 2D array - grid values in y direction
    data - numpy 2D array - potential data
    n - float - order of the derivative
    
    Output:
    yder - numpy 2D array - derivative in y direction
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape != data.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Condition for the order of the derivative
    assert n >= 0., 'Order of the derivative must be positive and nonzero!'
    
    if n == 0.:
        res = data
    else:    
        # Calculate the wavenuber in y direction
        _, ky = aux.wavenumber(x,y)
    
        # Apply the Fourier transform
        yder = np.fft.fft2(data)*((ky*1j)**(n))
        # Calculate the inverse transform
        res = np.real(np.fft.ifft2(yder))
    
    # Return the final output
    return res

def zderiv(x, y, data, n):
    
    '''
    Return the vertical derivative in z direction for n order in Fourier domain.
    
    Inputs:
    x - numpy 2D array - grid values in x direction
    y - numpy 2D array - grid values in y direction
    data - numpy 2D array - potential data
    n - float - order of the derivative
    
    Output:
    zder - numpy 2D array - derivative in z direction    
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape != data.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Condition for the order of the derivative
    assert n >= 0., 'Order of the derivative must be positive and nonzero!'
    
    if n == 0.:
        res = data
    else:    
        # Calculate the wavenuber in z direction
        kx, ky = aux.wavenumber(x,y)
    
        # Apply the Fourier transform
        zder = np.fft.fft2(data)*(np.sqrt(kx**2 + ky**2)**(n))
    
        # Calculate the inverse transform
        res = np.real(np.fft.ifft2(zder))
    
    # Return the final output
    return res

def horzgrad(x, y, data):
    
    '''
    Return the horizontal gradient amplitude (HGA) for a potential data on a regular 
    grid. All calculation is done by using Fourier domain.
    
    Inputs:
    x - numpy 2D array - grid values in x direction
    y - numpy 2D array - grid values in y direction
    data - numpy 2D array - potential data
    
    Output:
    hga - numpy 2D array - horizontal gradient amplitude
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape != data.shape:
        raise ValueError("All inputs must have same shape!")
    
    # Computes the horizontal derivatives
    diffx = xderiv(x, y, data, 1)
    diffy = yderiv(x, y, data, 1)
    
    # Calculates the total gradient
    hga = (diffx**2 + diffy**2)**(0.5)
    
    # Return the final output
    return hga

def totalgrad(x, y, data):
    
    '''
    Return the total gradient amplitude (TGA) for a potential data on a regular grid.
    
    Inputs:
    x - numpy 2D array - grid values in x direction
    y - numpy 2D array - grid values in y direction
    data - numpy 2D array - potential data
    
    Output:
    tga - numpy 2D array - total gradient amplitude
    '''
    
    # Stablishing some conditions
    if x.shape != y.shape != data.shape:
        raise ValueError("All inputs must have same shape!")

    # Calculates the x derivative
    diffx = xderiv(x, y, data, 1)
    # Calculates the y derivative
    diffy = yderiv(x, y, data, 1)
    # Calculates the z derivative
    diffz = zderiv(x, y, data, 1)

    # Calculates the total gradient
    tga = (diffx**2 + diffy**2 + diffz**2)**(0.5)
    
    # Return the final output
    return tga