import cv2
import numpy as np
import time
import scipy.spatial as spatial
import functools
import time
from random import randint

class Segmentation:
    def __init__(self,path,radius=100):
        self.path = path
        self.radius=int(radius)
    def readImage(self):
        self.img= cv2.imread(self.path)
    def create_data(self):
        h,w = self.img.shape[:2]
        # isExist={}
        dataX = []
        for i in range(h):
            for j in range(w):
                temp = np.concatenate((self.img[i,j],[i,j]))
                dataX.append(temp)
        self.data= dataX
    def distance_2_vectors(self,vec1, vec2):
        return np.linalg.norm(np.array(vec1)-np.array(vec2))
    def meanshift(self):
        posCenter = self.data
        result=[]
        inter = 1
        threshold = self.radius
        while len(posCenter)>0:
            i = randint(0,len(posCenter)-1)
            point_tree = spatial.cKDTree(posCenter,balanced_tree=False)
            currentPoint = posCenter[i]
            while(True):
                index = point_tree.query_ball_point(currentPoint,threshold)
                sumPoints =0
                for x in index:rray(vec2)
    def meanshift(self):
        posCenter = self.data
        result=[]
        inter = 1
        threshold = self.radius
        # posCenter = np.copy(dataX).tolist()
        while len(posCenter)>0:
            i = randint(0,len(posCenter)-1)
            point_tree = spatial.cKDTree(posCenter,balanced_tree=False)
            currentPoint = posCenter[i]
            while(True):
                index = point_tree.query_ball_point(currentPoint,threshold)
                sumPoints =0
                for x in index:
                    sumPoints = sumPoints+posCenter[x]
                newX = sumPoints/len(index)
                if self.distance_2_vectors(newX,currentPoint)<=inter:
                    index.sort(reverse=True)
                    tempList = []
                    tempList.append(newX)
                    for temp in index:
                        tempList.append(posCenter.pop(temp))
                    result.append(tempList)
                    break
                else:
                    currentPoint= newX
        return result
    def find_index_nearest(self,result,temp):
        minDistance= 9999999999
        index =-1
        for i in range(len(result)):
            distance =self.distance_2_vectors(result[i][0],temp)
            if minDistance>distance:
                minDistance=distance
                index=i
        return index
    def excute(self):
        pathlog = self.path[0:self.path.rfind('/')]
        self.readImage()
        self.create_data()
        begin = time.time()
        num = len(self.data)
        resultTemp = self.meanshift()
        timeResult = time.time()-begin
        img_result = self.img.copy()
        result=[]
        for i in range(len(resultTemp))[::-1]:
            if len(resultTemp[i])/num>=0.05:
                result.append(resultTemp.pop(i))
        if len(result)<=1:
            result=resultTemp
        else:
            for i in range(len(resultTemp))[::-1]:
                index = self.find_index_nearest(result,resultTemp[i][0])
                result[index]= result[index]+resultTemp.pop(i)[1:]

        img_result = self.img.copy()

        for  i in result:
            color = [int(temp) for temp in i[0][:3]]
            for j in i[1:]:
                img_result[j[3],j[4]] = color
        for index,i in enumerate(result):
            cv2.putText(img_result,str(index), (int(i[0][4]),int(i[0][3])), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2)
        cv2.imwrite(pathlog+'/Segmented_image.jpg',img_result)
        return pathlog+'/Segmented_image.jpg',[len(result),timeResult,num,pathlog+'/Segmented_image.jpg']

def main():
    obj = Segmentation('image.jpg','100')
    _,result = obj.excute()
if __name__ == '__main__':
    main()
