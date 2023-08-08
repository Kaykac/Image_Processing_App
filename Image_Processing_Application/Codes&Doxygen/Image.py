"""
The "Image" class in this code is derived from the "Ui_MainWindow" class.
This code is the piece of code that contains the image processing principles.
It also uses image manipulation libraries such as skimage, matplotlib, and PIL.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

import matplotlib.pyplot as plt
from skimage import data, img_as_float, io, color, segmentation, filters
from skimage.segmentation import chan_vese, morphological_chan_vese, morphological_geodesic_active_contour, checkerboard_level_set
from skimage.filters import threshold_multiotsu
from skimage.morphology import disk, binary_opening
from skimage.util import compare_images
from PIL import Image
import skimage
import pylab as plt
import numpy as np
import cv2
import matplotlib.image as mpimg
import colorsys
from skimage.color import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
import skimage.io
from skimage.color import rgb2hsv

from LabV2 import Ui_MainWindow

class Image(Ui_MainWindow):
    def __init__(self, MainWindow):
        super(Image, self).__init__()
        self.setupUi(MainWindow)

    
      
                        
        self.toolButton_C1.setEnabled(False)
        self.toolButton_C2.setEnabled(False)
        self.toolButton_Seg1.setEnabled(False)
        self.toolButton_Seg2.setEnabled(False)
        self.toolButton_Seg3.setEnabled(False)
        self.toolButton_E1.setEnabled(False)
        self.toolButton_E2.setEnabled(False)
        self.toolButton_E3.setEnabled(False)
        self.toolButton_E4.setEnabled(False)
        self.toolButton_S3.setEnabled(False)
        self.toolButton_O4.setEnabled(False)
        self.toolButton_O5.setEnabled(False)
        self.toolButton_O6.setEnabled(False)
        
        

        self.action_Exit.triggered.connect(MainWindow.close)     
  
        self.toolButton_S1.clicked.connect(self.openFile)
        self.action_Open_Source.triggered.connect(self.openFile)
        
        self.toolButton_C2.clicked.connect(self.RGBtoHSV)
        self.action_RGB_to_HSV.triggered.connect(self.RGBtoHSV)
        
        self.toolButton_C1.clicked.connect(self.RGBtoGrayScale)
        self.action_RGB_to_Grayscale.triggered.connect(self.RGBtoGrayScale)
        
        self.toolButton_Seg2.clicked.connect(self.ChanVese_Seg)
        self.action_Chan_Vese_Segmentation.triggered.connect(self.ChanVese_Seg)
        
        self.toolButton_Seg1.clicked.connect(self.MultiOtsu)
        self.action_Multi_Otsu_Thresholding.triggered.connect(self.MultiOtsu)
        
        self.toolButton_Seg3.clicked.connect(self.Morphological_Snakes)
        self.action_Morphological_Snakes.triggered.connect(self.Morphological_Snakes) 
        
        self.toolButton_E1.clicked.connect(self.Roberts)
        self.action_Roberts.triggered.connect(self.Roberts)       
        
        self.toolButton_E2.clicked.connect(self.Sobel)
        self.action_Sobel.triggered.connect(self.Sobel) 
        
        self.toolButton_E3.clicked.connect(self.Scharr)
        self.action_Scharr.triggered.connect(self.Scharr)     
        
        self.toolButton_E4.clicked.connect(self.Prewitt)
        self.action_Prewitt.triggered.connect(self.Prewitt)  
        
        self.toolButton_S2.clicked.connect(self.exportAs_Out)
        self.action_Output.triggered.connect(self.exportAs_Out)  

        self.action_Source.triggered.connect(self.exportAs)  
        self.toolButton_O3.clicked.connect(self.exportAs)       
        
        self.toolButton_O1.clicked.connect(self.saveOutput)
        self.action_Save_Output.triggered.connect(self.saveOutput)  
        
        self.toolButton_O2.clicked.connect(self.saveAsOutput)
        self.action_save_As_Output.triggered.connect(self.saveAsOutput)  
        
        self.toolButton_S3.clicked.connect(self.clearSource)
        self.action_Source_2.triggered.connect(self.clearSource)
        
        self.toolButton_O4.clicked.connect(self.ClearOut)
        self.actionO_Output.triggered.connect(self.ClearOut)
        
            
            
            
           
    ## @brief Performs the file decompression and loads the image.
    #  @details Allows the user to select a file and loads the selected image.
    #  @return None
    def openFile(self):
        # Opens the file selection dialog and gets the name of the selected file
        file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "JPEG Files (*.jpeg *.jpg);;PNG Files (*.png)")
    
        if check:
            # Loads the selected file into the QPixmap object
            pixmap = QPixmap(file)
    
            # QLabel üzerinde görüntüyü ayarlar ve boyutunu ayarlar
            self.label_Source.setPixmap(pixmap)
            self.label_Source.adjustSize()
    
            # Sets and resizes image on QLabel
            self.label_Output.setPixmap(pixmap)
            self.label_Output.adjustSize()
    
            # Enables accessibility to other functions
            self.action_Save_Output.setEnabled(True)
            self.action_save_As_Output.setEnabled(True)
            self.action_Undo_Output.setEnabled(True)
            self.action_Redo_Output.setEnabled(True)
            self.action_RGB_to_Grayscale.setEnabled(True)
            self.action_RGB_to_HSV.setEnabled(True)
            self.action_Multi_Otsu_Thresholding.setEnabled(True)
            self.action_Chan_Vese_Segmentation.setEnabled(True)
            self.action_Morphological_Snakes.setEnabled(True)
            self.action_Output.setEnabled(True)
            self.action_Source.setEnabled(True)
            self.action_Source_2.setEnabled(True)
            self.actionO_Output.setEnabled(True)
    
            self.toolButton_C1.setEnabled(True)
            self.toolButton_C2.setEnabled(True)
            self.toolButton_Seg1.setEnabled(True)
            self.toolButton_Seg2.setEnabled(True)
            self.toolButton_Seg3.setEnabled(True)
            self.toolButton_S3.setEnabled(True)
            self.toolButton_O4.setEnabled(True)
            self.toolButton_O5.setEnabled(True)
            self.toolButton_O6.setEnabled(True)
    
            # Saves the selected file as 'Output.png'
            img = Image.open(file)
            img = img.save("Output.png")
    
            # Saves the selected file as 'Source.png'
            img1 = Image.open(file)
            img1 = img1.save("Source.png")



        
                 




    ## @brief Cleans the output and loads the startup image.
    #  @details Cleans the output and reloads the startup image to its original state.
    #  @return None
    def ClearOut(self):
        # Loads 'Source.png' and saves to 'Output.png'
        img1 = Image.open("Source.png")
        img1 = img1.save("Output.png")
    
        # Sets and resizes image on QLabel
        pixmap = QPixmap("Source.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
        # Disables accessibility to other functions
        self.toolButton_E1.setEnabled(False)
        self.toolButton_E2.setEnabled(False)
        self.toolButton_E3.setEnabled(False)
        self.toolButton_E4.setEnabled(False)
    
        self.action_Roberts.setEnabled(False)
        self.action_Scharr.setEnabled(False)
        self.action_Sobel.setEnabled(False)
        self.action_Prewitt.setEnabled(False)
    
    ## @brief Exports the image in the specified format.
    #  @details Exports the image in the specified format and gives the user a way to save it.
    #  @return None
    def exportAs(self):
        label = self.label_Source
        pixmap = label.pixmap()
    
        if pixmap:
            # Provides the user with a way to save the file
            file, _ = QFileDialog.getSaveFileName(None, "Dosya Kaydet", "", "PNG Dosyaları (*.png);;JPEG Dosyaları (*.jpeg)")
    
            if file:
                # Saves the QPixmap in the specified file format
                pixmap.save(file)
    
    ## @brief Exports the output in the specified format.
    #  @details Exports the output in the specified format and gives the user a way to save it.
    #  @return None
    def exportAs_Out(self):
        label = self.label_Output
        pixmap = label.pixmap()
    
        if pixmap:
            # Provides the user with a way to save the file
            file, _ = QFileDialog.getSaveFileName(None, "Dosya Kaydet", "", "PNG Dosyaları (*.png);;JPEG Dosyaları (*.jpeg)")
    
            if file:
                # Saves the QPixmap in the specified file format
                pixmap.save(file)
    
    ## @brief Saves the output to the 'Output.png' file.
    #  @details Saves the output to the 'Output.png' file.
    #  @return None
    def saveOutput(self):
        label = self.label_Output
        pixmap = label.pixmap()
    
        if pixmap:
            file = "Output.png"
            # Saves QPixmap to 'Output.png'
            pixmap.save(file, "PNG")
    
    ## @brief Saves the output in the specified name and format.
    #  @details Saves the output in the specified name and format.
    #  @return None
    def saveAsOutput(self):
        label = self.label_Output
        pixmap = label.pixmap()
    
        if pixmap:
            # Provides the user with a way to save the file
            file, _ = QFileDialog.getSaveFileName(None, "Dosya Kaydet", "Output", "PNG Dosyaları (*.png);;JPEG Dosyaları (*.jpeg)")
    
            if file:
                # Saves the QPixmap in the specified file format
                pixmap.save(file)

    ## @brief Makes the output image grayscale.
    #  @details Makes the output image grayscale and saves it to the 'Output.png' file.
    #  @return None
    def RGBtoGrayScale(self):
        # Enables accessibility to other functions
        self.toolButton_E1.setEnabled(True)
        self.toolButton_E2.setEnabled(True)
        self.toolButton_E3.setEnabled(True)
        self.toolButton_E4.setEnabled(True)
    
        self.action_Roberts.setEnabled(True)
        self.action_Scharr.setEnabled(True)
        self.action_Sobel.setEnabled(True)
        self.action_Prewitt.setEnabled(True)
    
        # Loads 'output.png'
        image = io.imread('Output.png')
        gray_image = color.rgb2gray(image)
        # Saves the grayscale image to the 'Output.png' file
        io.imsave('Output.png', gray_image)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Converts the output image to HSV color space.
    #  @details Converts the output image to HSV color space and saves it to the 'Output.png' file.
    #  @return None
    def RGBtoHSV(self):
        # Loads 'output.png'
        image = io.imread('Output.png')
        hsv_image = color.rgb2hsv(image)
        # Saves image to 'Output.png' in HSV color space
        io.imsave('Output.png', hsv_image)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Cleans the source and output images.
    #  @details Clears source and output images, disables button and menu functions.
    #  @return None
    def clearSource(self):
        # Clears image in QLabel
        self.label_Source.clear()
        self.label_Output.clear()
    
        # Disables accessibility to other functions
        self.action_Save_Output.setEnabled(False)
        self.action_save_As_Output.setEnabled(False)
        self.action_Undo_Output.setEnabled(False)
        self.action_Redo_Output.setEnabled(False)
        self.action_RGB_to_Grayscale.setEnabled(False)
        self.action_RGB_to_HSV.setEnabled(False)
        self.action_Multi_Otsu_Thresholding.setEnabled(False)
        self.action_Chan_Vese_Segmentation.setEnabled(False)
        self.action_Morphological_Snakes.setEnabled(False)
        self.action_Output.setEnabled(False)
        self.action_Source.setEnabled(False)
        self.action_Source_2.setEnabled(False)
        self.actionO_Output.setEnabled(False)
        self.action_Roberts.setEnabled(False)
        self.action_Scharr.setEnabled(False)
        self.action_Sobel.setEnabled(False)
        self.action_Prewitt.setEnabled(False)
        self.toolButton_C1.setEnabled(False)
        self.toolButton_C2.setEnabled(False)
        self.toolButton_Seg1.setEnabled(False)
        self.toolButton_Seg2.setEnabled(False)
        self.toolButton_Seg3.setEnabled(False)
        self.toolButton_E1.setEnabled(False)
        self.toolButton_E2.setEnabled(False)
        self.toolButton_E3.setEnabled(False)
        self.toolButton_E4.setEnabled(False)
        self.toolButton_O5.setEnabled(False)
        self.toolButton_O6.setEnabled(False)

        
        
              
    ## @brief Applies the multiple Otsu thresholding method on the output image.
    #  @details Applies multiple Otsu thresholding method on output image and saves to 'Output.png' file.
    #  @return None
    def MultiOtsu(self):
        # Loads 'output.png'
        image = io.imread('Output.png')
        thresholds = threshold_multiotsu(image)
        regions = np.digitize(image, bins=thresholds)
        # Multi Otsu saves thresholding result to 'Output.png'
        io.imsave('Output.png', regions)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Implements the Chan-Vese segmentation method.
    #  @details Implements the Chan-Vese segmentation method, saves it to the 'Output.png' file and displays the image.
    #  @return None
    def ChanVese_Seg(self):
        # Loads 'output.png'
        image = io.imread('Output.png')
        gray_image = color.rgb2gray(image)
        segmented = segmentation.chan_vese(gray_image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3, max_iter=200, dt=0.5)
        binary_mask = np.where(segmented, 255, 0).astype(np.uint8)
        # Saves Chan-Vese segmentation result to 'Output.png'
        io.imsave('Output.png', binary_mask)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Implements the morphological snakes algorithm.
    #  @details Applies the morphological snakes algorithm, saves it to the 'Output.png' file and displays the image.
    #  @return None
    def Morphological_Snakes(self):
        # Loads 'output.png'
        image = io.imread('Output.png')
        gray_image = color.rgb2gray(image)
        segmented = morphological_chan_vese(gray_image, iterations=200, init_level_set="checkerboard", smoothing=1, lambda1=1, lambda2=1)
        selem = disk(3)
        post_processed = binary_opening(segmented, selem)
        binary_mask = np.where(post_processed, 255, 0).astype(np.uint8)
        # Saves morphological snakes result in 'Output.png'
        io.imsave('Output.png', binary_mask)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Roberts implements the edge detection method.
    #  @details Roberts implements the edge detection method, saves it to the 'Output.png' file and displays the image.
    #  @return None
    def Roberts(self):
        # Loads 'output.png'
        image = io.imread('Output.png')
        edge_image = filters.roberts(image)
        # Roberts saves edge detection result in 'Output.png'
        io.imsave('Output.png', edge_image)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Implements the Sobel edge detection method.
    #  @details Sobel implements edge detection method, saves to 'Output.png' file and displays the image.
    #  @return None
    def Sobel(self):
        # Loads 'output.png'.
        image = io.imread('Output.png')
        edge_image = filters.sobel(image)
        # Sobel saves edge detection result in 'Output.png'
        io.imsave('Output.png', edge_image)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Implements the Scharr edge detection method.
    #  @details Scharr implements edge detection method, saves to 'Output.png' file and displays the image.
    #  @return None
    def Scharr(self):
        # 'Loads 'output.png'.
        image = io.imread('Output.png')
        edge_image = filters.scharr(image)
        # Scharr saves edge detection result in 'Output.png'
        io.imsave('Output.png', edge_image)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()
    
    ## @brief Implements the Prewitt edge detection method.
    #  @details Prewitt implements edge detection method, saves to 'Output.png' file and displays the image.
    #  @return None
    def Prewitt(self):
        # 'Loads 'output.png'.
        image = io.imread('Output.png')
        edge_image = filters.prewitt(image)
        # Prewitt saves edge detection result in 'Output.png'
        io.imsave('Output.png', edge_image)
        pixmap = QPixmap("Output.png")
        self.label_Output.setPixmap(pixmap)
        self.label_Output.adjustSize()

