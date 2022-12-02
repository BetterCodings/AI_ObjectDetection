package com.example.software_application_design

import android.annotation.SuppressLint
import android.app.Activity
import android.content.Intent
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.main.*
import kotlinx.android.synthetic.main.main.searchBtn
import kotlinx.android.synthetic.main.modify.*

class modify : AppCompatActivity() {
    @SuppressLint("ResourceAsColor")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.modify)

        var count: Int = 3;
        people.text = "현 출석 인원: $count"

        o1Btn.setOnClickListener {
            o1Btn.isEnabled = false
            x1Btn.isEnabled = true
            o1Btn.setTextColor(R.color.home)
            x1Btn.setTextColor(Color.BLACK)
            count += 1
            people.text = "현 출석 인원: $count"
        }
        x1Btn.setOnClickListener {
            x1Btn.isEnabled = false
            o1Btn.isEnabled = true
            o1Btn.setTextColor(Color.BLACK)
            x1Btn.setTextColor(Color.RED)
            count -= 1
            people.text = "현 출석 인원: $count"
        }
        o2Btn.setOnClickListener {
            o2Btn.isEnabled = false
            x2Btn.isEnabled = true
            o2Btn.setTextColor(R.color.home)
            x2Btn.setTextColor(Color.BLACK)
            count += 1
            people.text = "현 출석 인원: $count"
        }
        x2Btn.setOnClickListener {
            x2Btn.isEnabled = false
            o2Btn.isEnabled = true
            o2Btn.setTextColor(Color.BLACK)
            x2Btn.setTextColor(Color.RED)
            count -= 1
            people.text = "현 출석 인원: $count"
        }
        o3Btn.setOnClickListener {
            o3Btn.isEnabled = false
            x3Btn.isEnabled = true
            o3Btn.setTextColor(R.color.home)
            x3Btn.setTextColor(Color.BLACK)
            count += 1
            people.text = "현 출석 인원: $count"
        }
        x3Btn.setOnClickListener {
            x3Btn.isEnabled = false
            o3Btn.isEnabled = true
            o3Btn.setTextColor(Color.BLACK)
            x3Btn.setTextColor(Color.RED)
            count -= 1
            people.text = "현 출석 인원: $count"
        }

        searchBtn.setOnClickListener {
            var intent = Intent()
            intent.putExtra("count", count.toString())
            setResult(Activity.RESULT_OK, intent)
            finish()
        }
    }
}