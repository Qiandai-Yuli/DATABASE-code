import time
abcs=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ABCs=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums=['1','2','3','4','5','6','7','8','9','0']
dots=[',','.','?','!','(',')','+','-','=','@','%','_','*','/','·','、','。','《','》','<','>','^']
result=[]
s=[]

def encrypt_alpha():
	i=1
	i_r=0
	E_ori=input("input the text:")
	p=eval(input("input the password number:"))
	for l in E_ori:
		i_l=0
		#
		while i_l<=25:
			tp=0
			if l==abcs[i_l]:
				tp=(i_l+p)%25
				result.append(abcs[tp])
				break
			elif l==ABCs[i_l]:
				tp=(i_l+p)%25
				result.append(ABCs[tp])
				break
			elif l in nums or l in dots:
				result.append(l)
				break
			elif l==' ':
				result.append(' ')
				break
			i_l+=1
	while i_r<=len(E_ori)-1:
		print(result[i_r],end='')
		i_r+=1








def encrypt_beta():
	i=1
	i_r=0
	E_ori=input("input the ciphertext:")
	p=eval(input("input the password number:"))
	for l in E_ori:
		i_l=0
		#
		while i_l<=25:
			tp=0
			if l==abcs[i_l]:
				tp=(i_l+p)%25
				result.append(abcs[tp])
				break
			elif l==ABCs[i_l]:
				tp=(i_l+p)%25
				result.append(ABCs[tp])
				break
			elif l in nums or l in dots:
				result.append(l)
				break
			elif l==' ':
				result.append(' ')
				break
			i_l+=1
	while i_r<=len(E_ori)-1:
		print(result[-1-i_r],end='')
		i_r+=1

def encrypt_gamma():
	i_1=1
	i_r=0
	E_ori=input("input the text:")
	p=eval(input("input the password number:"))
	if p>=len(E_ori):
		print("---error---")
	else:
		pass
	for l in E_ori:
		if l==' ':
			pass
		else:
			s.append(l)
	p_1=len(s)//p
	p_2=len(s)%p
	while i_1<=p:
		if i_1<=p_2:
			i_2=1
			while i_2<=p_1+1:
				result.append(s[i_1-1+p*(i_2-1)])
				i_2+=1
			i_1+=1
		else:
			i_2=1
			while i_2<=p_1:
				result.append(s[i_1-1+p*(i_2-1)])
				i_2+=1
			i_1+=1
	while i_r<=len(E_ori)-1:
		print(result[i_r],end='')
		i_r+=1







def decode_alpha():
	i=1
	i_r=0
	E_ori=input("input the text:")
	p=eval(input("input the password number:"))
	for l in E_ori:
		i_l=0
		#
		while i_l<=25:
			tp=0
			if l==abcs[i_l]:
				tp=(i_l-p)%25
				result.append(abcs[tp])
				break
			elif l==ABCs[i_l]:
				tp=(i_l-p)%25
				result.append(ABCs[tp])
				break
			elif l in nums or l in dots:
				result.append(l)
				break
			elif l==' ':
				result.append(' ')
				break
			i_l+=1
	while i_r<=len(E_ori)-1:
		print(result[i_r],end='')
		i_r+=1



def decode_beta():
	i=1
	i_r=0
	E_ori=input("input the ciphertext:")
	p=eval(input("input the password number:"))
	for l in E_ori:
		i_l=0
		#
		while i_l<=25:
			tp=0
			if l==abcs[i_l]:
				tp=(i_l-p)%25
				result.append(abcs[tp])
				break
			elif l==ABCs[i_l]:
				tp=(i_l-p)%25
				result.append(ABCs[tp])
				break
			elif l in nums or l in dots:
				result.append(l)
				break
			elif l==' ':
				result.append(' ')
				break
			i_l+=1
	while i_r<=len(E_ori)-1:
		print(result[-1-i_r],end='')
		i_r+=1


























def main():
	print('-----Welcome to this password application!-----')
	print('input "e" to encrypt or input "d" to decode or "q" to quit')
	dec=input("decision:")
	if dec=="e":
		print("-----Encrypt Mode-----")
		print("choose the encrypt pattern(alpha , beta or gamma) or input 'q' to return the previous level")
		dec_se=input("decision:")
		if dec_se=="alpha":
			encrypt_alpha()
		elif dec_se=="beta":
			encrypt_beta()
		elif dec_se=="gamma":
			encrypt_gamma()
		elif dec_se=="q":
			main()
		else:
			print("---error---")
	elif dec=="d":
		print("-----Decode Mode-----")
		print("choose the decode pattern(alpha or beta) or input 'q' to return the previous level")
		dec_se=input("decision:")
		if dec_se=="alpha":
			decode_alpha()
		elif dec_se=="beta":
			decode_beta()
		elif dec_se=="gamma":
			print("decode_gamma() is being written")
		elif dec_se=="q":
			main()
		else:
			print("---error---")
	elif dec=="q":
		time.sleep(2)
		quit()
	else:
		print("---error---")


main()


