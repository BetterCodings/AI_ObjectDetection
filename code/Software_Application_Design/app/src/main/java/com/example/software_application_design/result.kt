package com.example.software_application_design

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import kotlinx.android.synthetic.main.modify.*
import kotlinx.android.synthetic.main.result.*
import kotlinx.android.synthetic.main.search.*
import kotlinx.android.synthetic.main.search.okBtn

class result : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.result)

        modBtn.setOnClickListener {
            var intent = Intent(this, modify::class.java)
            startActivityForResult(intent, 100)
        }

        okBtn.setOnClickListener {
            var intent = Intent(this, search::class.java)
            startActivity(intent)
        }
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (resultCode == Activity.RESULT_OK) {
            when (requestCode) {
                100 -> {
                    var count = data!!.getStringExtra("count").toString()
                    nowPeople.text = "현재 인원: $count 명"
                    if(count.toInt() < 3){
                        resultPeople.text = "결과: 결석자 존재"
                    }
                    else{
                        resultPeople.text = "결과: 전원 출석"
                    }
                }
            }
        }
    }
}