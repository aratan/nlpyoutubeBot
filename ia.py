import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle

# ---------- Cosas a descargar para que ntlk funcione correctamente en Inglés----------
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
#--------------------------------------------------------------------------------------

ruta_modelo = './modelito.pkl'
loaded_model = pickle.load(open(ruta_modelo, 'rb'))

# Creamos una función con la limpieza de datos
def limpiaTexto(texto):
   lemmatize=nltk.WordNetLemmatizer()
   # Eliminamos espacios blancos
   texto.replace(u'\xa0', u' ')
   texto.strip()
   #Comprobar los caracteres para ver si están en la puntuación
   nopunc = [char for char in texto if char not in string.punctuation]
   # Vuelve a unir los caracteres para formar la cadena.
   nopunc = ''.join(nopunc)
   # Lemmatizar las palabras
   nopunc = [lemmatize.lemmatize(word) for word in nopunc.split()]
   # Vuelve a unir los caracteres para formar la cadena.
   nopunc = ' '.join(nopunc)
   # Ahora sólo hay que eliminar las palabras de parada
   return [word.lower() for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# estamos entrenando otro tfidf, se debe usar el de entrenamiento
# utilizamos solo bow o tfidf

def preparaTexto(texto):
   input = [f"{texto}"] 
   ruta_transformer = './transformer.pkl'
   #ruta_transformer = './models/tfidftransformer.pkl'
   loaded_transformer = pickle.load(open(ruta_transformer, 'rb'))
   text_bow = loaded_transformer.transform(input)
   X = text_bow
   return X

# Función para predicción de toxicidad
def prediceToxico(texto):
   prediccion = loaded_model.predict(preparaTexto(texto))
   print(prediccion)
   if prediccion == 1:
     print("Deben tomarse medidas.")
     return "Deben tomarse medidas."
   else:
      print("Este mensaje no parece ser tóxico")
      return "Deben tomarse medidas."
      
# Texto de ejemplo
## texto = "The cat meowed"

#prediceToxico(texto)        