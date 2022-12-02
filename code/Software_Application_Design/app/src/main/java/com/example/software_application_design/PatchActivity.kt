package com.example.software_application_design

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class PatchActivity: AppCompatActivity() {
    internal lateinit var retrofit: Retrofit
    internal lateinit var apiService: ApiService
    internal lateinit var comment: Call<Json_Test_Java>
    internal lateinit var result: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        retrofit = Retrofit.Builder().baseUrl(ApiService.API_URL).addConverterFactory(GsonConverterFactory.create()).build()
        apiService = retrofit.create(ApiService::class.java)
        val version = Json_Test_Java("test5")

        comment = apiService.post_json_test_java("json", version)
        comment.enqueue(object: Callback<Json_Test_Java> {
            override fun onResponse(call: Call<Json_Test_Java>, response: Response<Json_Test_Java>) {
                Log.e("D_Test", "2차")
                if (response.isSuccessful) {
                    Log.e("post", "성공")
                }
                else {
                    val StatusCode = response.code()
                    Log.e("post", "Status Code: $StatusCode")
                }
            }

            override fun onFailure(call: Call<Json_Test_Java>, t: Throwable) {
                result = "error!!"
                Log.e("D_Test", "페일!")
            }
        })
    }
}