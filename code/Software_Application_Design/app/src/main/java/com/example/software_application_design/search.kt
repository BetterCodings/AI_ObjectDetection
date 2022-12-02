package com.example.software_application_design

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.search.*

class search : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.search)

        tues1Btn.setOnClickListener {
            var intent = Intent(this, result::class.java)
            startActivity(intent)
        }

        tues2Btn.setOnClickListener {
            var intent = Intent(this, result::class.java)
            startActivity(intent)
        }

        thurs1Btn.setOnClickListener {
            var intent = Intent(this, result::class.java)
            startActivity(intent)
        }

        thurs2Btn.setOnClickListener {
            var intent = Intent(this, result::class.java)
            startActivity(intent)
        }

        okBtn.setOnClickListener {
            var intent = Intent(this, main::class.java)
            startActivity(intent)
        }
    }


}