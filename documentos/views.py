# -*- coding: utf-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from documentos.models import *
from documentos.forms import *
import nltk
from nltk.corpus import cess_esp
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import SnowballStemmer


def home(request):

	lista_documentos = Documento.objects.all().order_by('id')[:5]
	resultado = ""

	if request.method == 'POST':
		form = SubirDocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			#handle_uploaded_file(request.FILES['contenido'])
			resultado = "form valido"
	else:
		form = SubirDocumentoForm()

	return render_to_response('templates/index.html', {'lista_documentos': lista_documentos, 'form': form})


def procesar(request, identificador):
	lmtzr = WordNetLemmatizer()
	d = Documento.objects.get(id=identificador)
	
	#nltk.corpus.cess_esp.words()
	
	
	tokens = nltk.word_tokenize(d.contenido.replace('.', ' . '))
	#print tokens
	#scentence = d.contenido

	#scentence = scentence.lower() 

	words = tokens
	spanish_stemmer = SnowballStemmer('spanish')
	

	#This is the simple way to remove stop words
	important_words=[]
	for word in words:
		if word not in stopwords.words('spanish'):
		    important_words.append([word, lmtzr.lemmatize(word), spanish_stemmer.stem(word)])




	return render_to_response('templates/documentoProcesado.html', 
				{
					'original': d.contenido,
					'tokens': tokens,
					'important_words' : important_words,
					#'pos_tags': pos_tags,
					#'ne_chunks': ne_chunks.subtrees(),
				})
	
	
