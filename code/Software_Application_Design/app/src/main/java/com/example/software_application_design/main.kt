package com.example.software_application_design

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.widget.Toast
import kotlinx.android.synthetic.main.main.*

class main : AppCompatActivity() {
    var handler: Handler? = null;
    var num: Int? = null;
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main)

        searchBtn.setOnClickListener {
            var intent = Intent(this, search::class.java)
            startActivity(intent)
        }

        cameraBtn.setOnClickListener {
            when(radioGroup.checkedRadioButtonId){
                R.id.sub1Btn -> {
                    Toast.makeText(this@main, "1번", Toast.LENGTH_SHORT).show()
                }
                R.id.sub2Btn -> {
                    Toast.makeText(this@main, "2번", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }
}