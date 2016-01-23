from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def games(request):
	return render(request, 'games.html', {})

def game2048(request):
	return render(request, '2048.html', {})

def gamebingohome(request):
	return render(request, 'bingohome.html', {})

def gamebingoplay(request):
	#form = BingoForm(request.POST or None)

	context = {

		"num11" : request.POST['num11'],
		"num12" : request.POST['num12'],
		"num13" : request.POST['num13'],
		"num14" : request.POST['num14'],
		"num15" : request.POST['num15'],
		"num21" : request.POST['num21'],
		"num22" : request.POST['num22'],
		"num23" : request.POST['num23'],
		"num24" : request.POST['num24'],
		"num25" : request.POST['num25'],
		"num31" : request.POST['num31'],
		"num32" : request.POST['num32'],
		"num33" : request.POST['num33'],
		"num34" : request.POST['num34'],
		"num35" : request.POST['num35'],
		"num41" : request.POST['num41'],
		"num42" : request.POST['num42'],
		"num43" : request.POST['num43'],
		"num44" : request.POST['num44'],
		"num45" : request.POST['num45'],
		"num51" : request.POST['num51'],
		"num52" : request.POST['num52'],
		"num53" : request.POST['num53'],
		"num54" : request.POST['num54'],
		"num55" : request.POST['num55'],
	}

	#print num11

	return render(request, 'bingoplay.html', context)

def gamebuttonmania(request):
	return render(request, 'buttonmania.html', {})	

def gamebatshoot(request):
	return render(request, 'batshoot.html', {})

def gamebrickbreaker(request):
	return render(request, 'brickbreaker.html', {})

def gametigerjump(request):
	return render(request, 'tigerjump.html', {})