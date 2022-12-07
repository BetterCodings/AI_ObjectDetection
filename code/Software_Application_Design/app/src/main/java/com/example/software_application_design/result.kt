package com.example.software_application_design

import android.content.Intent
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.os.Bundle
import android.os.Environment
import android.util.Log
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.result.*
import kotlinx.android.synthetic.main.search.okBtn
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody
import okhttp3.RequestBody.Companion.asRequestBody
import okhttp3.RequestBody.Companion.toRequestBody
import okhttp3.ResponseBody
import org.json.JSONArray
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.converter.scalars.ScalarsConverterFactory
import java.io.*
import java.lang.Exception
import java.util.*


class Result : AppCompatActivity() {
    internal lateinit var retrofit: Retrofit
    internal lateinit var subjectService: SubjectService
    internal lateinit var comment: Call<List<Subject>>
    internal lateinit var post: Call<ResponseBody>
    internal lateinit var result: Subject
    var RESULT_MODIFY = 1
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.result)

        retrofit = Retrofit.Builder()
            .baseUrl(SubjectService.BASE_URL)
            .addConverterFactory(ScalarsConverterFactory.create())
            .addConverterFactory(GsonConverterFactory.create())
            .build()
        subjectService = retrofit.create(SubjectService::class.java)

        val cal = Calendar.getInstance()
        val year = cal.get(Calendar.YEAR).toString()
        val month = (cal.get(Calendar.MONTH) + 1).toString()
        val day = cal.get(Calendar.DATE).toString()
        val hour = cal.get(Calendar.HOUR_OF_DAY).toString()
        val minute = cal.get(Calendar.MINUTE).toString()
        val second = cal.get(Calendar.SECOND).toString()
        var fileName = "${year}_${month}_${day}_${hour}_${minute}_${second}"
        var fileName_png = "${fileName}.jpg"

        if (intent.hasExtra("image")) {
            val byte = intent.getByteArrayExtra("image")
            val bitmap = BitmapFactory.decodeByteArray(byte, 0, byte!!.size)
            var path = Environment.getExternalStorageDirectory().toString() + File.separator + "Pictures/"
            var file = bitmapToFile(bitmap, path + fileName_png)

            Toast.makeText(this@Result, file.toString(), Toast.LENGTH_SHORT).show()
            Log.d("D_Test", file!!.path)
            resultImg.setImageBitmap(bitmap)

            val reqFile = file.asRequestBody("multipart/form-data".toMediaTypeOrNull())
            val body = MultipartBody.Part.createFormData("image", file.name, reqFile)
            val name = fileName.toRequestBody("text/plain".toMediaTypeOrNull())

            post = subjectService.postSubject(name, body)
            post.enqueue(object: Callback<ResponseBody> {
                override fun onResponse(call: Call<ResponseBody>, response: Response<ResponseBody>) {
                    var str = response.body()!!.string()
                    try{
                        var jsonArray = JSONArray(str)
                        for (i in 0 until jsonArray.length()) {
                            var jsonObject = jsonArray.getJSONObject(i)
                            Log.d("D_Test", jsonObject.get("ID").toString())
                        }
                    } catch (e: Exception){
                        e.printStackTrace()
                    }

                    Log.d("D_Test", "post성공: ${response.body()!!.string()}")
                    Toast.makeText(this@Result, response.body()!!.string(), Toast.LENGTH_SHORT).show()
                }

                override fun onFailure(call: Call<ResponseBody>, t: Throwable) {
                    Log.e("D_Test", "실패: $t")
                }
            })


        } else {
            Toast.makeText(this, "전달된 이름이 없습니다", Toast.LENGTH_SHORT).show()

            comment = subjectService.getSubject(fileName)
            comment.enqueue(object: Callback<List<Subject>> {
                override fun onResponse(call: Call<List<Subject>>, response: Response<List<Subject>>) {
                    Log.d("D_Test", "get성공: ${response.body()}")
                    Toast.makeText(this@Result, result.image.toString(), Toast.LENGTH_SHORT).show()
                }

                override fun onFailure(call: Call<List<Subject>>, t: Throwable) {
                    Log.e("D_Test", "실패: $t")
                }
            })
        }

        modBtn.setOnClickListener {
            var intent = Intent(this, Modify::class.java)
            startActivityForResult(intent, RESULT_MODIFY)
        }

        okBtn.setOnClickListener {
            var intent = Intent(this, Search::class.java)
            startActivity(intent)
        }
    }
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (resultCode == RESULT_MODIFY) {
            var count = data!!.getStringExtra("count").toString()
            nowPeople.text = "현재 인원: $count 명"
            if (count.toInt() < 3) {
                resultPeople.text = "결과: 결석자 존재"
            } else {
                resultPeople.text = "결과: 전원 출석"
            }
        }
    }


    fun bitmapToFile(bitmap: Bitmap, path: String): File{
        var file = File(path)
        var out: OutputStream? = null
        try{
            file.createNewFile()
            out = FileOutputStream(file)
            bitmap.compress(Bitmap.CompressFormat.PNG, 80, out)
        }finally{
            out?.close()
        }
        return file
    }


}