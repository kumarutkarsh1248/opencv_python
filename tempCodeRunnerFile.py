mask = cv.circle(blank, (img1.shape[1] // 2, img1.shape[0] // 2), 100, 255, -1)
cv.imshow("mask", mask)

# creating a msked image
masked_image = cv.bitwise_and(src1=img1, src2=img2, mask=mask)