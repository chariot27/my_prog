package com.chariot.nexus

import android.content.Intent
import android.os.Bundle
import android.text.Html
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import com.chariot.nexus.Models.User
import com.chariot.nexus.Utils.USER_NODE
import com.chariot.nexus.Utils.USER_PROFILE_FOLDER
import com.chariot.nexus.Utils.uploadImage
import com.chariot.nexus.databinding.ActivitySignUpBinding
import com.google.firebase.Firebase
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.auth
import com.google.firebase.firestore.firestore

@Suppress("DEPRECATION")
class SignUpActivity : AppCompatActivity() {
    private val binding by lazy {
        ActivitySignUpBinding.inflate(layoutInflater)
    }
    private lateinit var user: User
    private var launcher= registerForActivityResult(ActivityResultContracts.GetContent()){
        uri->
        uri?.let{
            uploadImage(uri, USER_PROFILE_FOLDER){
                if(it==null){
                    // 1 hora 27 minutos 42 segundos no video
                }else{
                    user.image=it
                    binding.profileImage.setImageURI(uri)
                }
            }
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)
        val text = "<font color=#FF000000>Você já possui uma conta? </font> <font color=#1E88E5>Login?</font>"
        binding.login.text = Html.fromHtml(text)
        user=User()
        binding.register.setOnClickListener {
            if (binding.name.editableText?.toString().equals("") or
                binding.email.editableText?.toString().equals("") or
                binding.senha.editableText?.toString().equals("")
                )
            {
                Toast.makeText(this@SignUpActivity,"Please fill all the information",Toast.LENGTH_SHORT).show()
            }else{
                FirebaseAuth.getInstance().createUserWithEmailAndPassword(
                    binding.email.editableText.toString(),
                    binding.senha.editableText.toString()
                ).addOnCompleteListener {
                    result->
                    if(result.isSuccessful){
                        user.name=binding.name.editableText?.toString()
                        user.senha=binding.senha.editableText?.toString()
                        user.email=binding.email.editableText?.toString()
                        Firebase.firestore.collection(USER_NODE)
                            .document(Firebase.auth.currentUser!!.uid)
                            .set(user).addOnSuccessListener{
                                startActivity(Intent(this@SignUpActivity,HomeActivity::class.java))
                            }
                    }else{
                        Toast.makeText(this@SignUpActivity, result.exception?.localizedMessage, Toast.LENGTH_SHORT).show()
                    }
                }
            }
        }
        binding.addImage.setOnClickListener {
            launcher.launch("image/*")
        }
        binding.login.setOnClickListener {
            startActivity(Intent(this@SignUpActivity,LoginActivity::class.java))
            finish()
        }
    }
}