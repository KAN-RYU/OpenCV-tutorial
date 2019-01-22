import cv2 as cv

cap = cv.VideoCapture('images/doit.mp4') #비디오를 불러오기

while(cap.isOpened()):
    #비디오에서 프레임단위로 읽어오기
    ret, frame = cap.read()

    #흑백으로 변환
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #한 프레임씩 출력
    cv.imshow('gray', gray) 

    #25ms 동안 키입력 대기, 프레임시간이 됨.
    if cv.waitKey(25) & 0xFF == 27: 
        break

#모든 객체 해제
cap.release()
cv.destroyAllWindows()