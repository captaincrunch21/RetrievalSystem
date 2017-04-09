import tf_idf as tf
model = tf.model("C:\Users\dastan\Downloads\en.docs.2011.tar_1_\en.docs.2011\en_BDNews24\en_BDNews24\\1")
model.modelMaker()
model.makePickle()
import pickle
pickle.dump(model,open('model.pkl','wb'))
