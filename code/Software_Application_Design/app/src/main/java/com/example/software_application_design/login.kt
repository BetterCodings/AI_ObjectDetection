package com.example.software_application_design

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.login.*

class login : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.login)

        loginBtn.setOnClickListener {
            if(userId.text.toString() == "" && userPw.text.toString() == ""){
                var intent = Intent(this, main::class.java)
                startActivity(intent)
            }
            else{
                Toast.makeText(this@login, "오류입니다", Toast.LENGTH_SHORT).show();
            }
        }
    }


}