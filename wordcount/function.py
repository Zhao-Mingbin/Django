from django.shortcuts import render

def home(request):
	return render(request,'home.html')
def count(request):
	#返回输入的字符长度
	total_count=len(request.GET['text'])
	#返回输入的内容
	user_text=request.GET['text']
	#比较出现频率
	word_dic={}
	for word in user_text:
		if word not in word_dic:
			word_dic[word]=1
		elif word in word_dic:
			word_dic[word]+=1
	word_dic=sorted(word_dic.items(), key=lambda w:w[1] ,reverse= True)
	most_leter=word_dic[0][0]
	return render(request, 'count.html',{'count':total_count,
	                                     'content':user_text,
	                                     'wordDic':word_dic,
	                                     'most_leter':most_leter})
def about(request):
	return render(request,'about.html')