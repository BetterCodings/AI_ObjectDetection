package com.example.software_application_design

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import java.lang.Exception

class DeleteActivity: AppCompatActivity() {
    internal lateinit var retrofit: Retrofit
    internal lateinit var apiService: ApiService
    internal lateinit var comment: Call<ResponseBody>
    internal lateinit var result: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        retrofit = Retrofit.Builder().baseUrl(ApiService.API_URL).build()
        apiService = retrofit.create(ApiService::class.java)
        comment = apiService.delete_Patch_Test(2, "json")
        comment.enqueue(object: Callback<ResponseBody> {
            override fun onResponse(call: Call<ResponseBody>, response: Response<ResponseBody>) {
                try {
                    //Log.e("D_Test", response.body()!!.string())

                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }

            override fun onFailure(call: Call<ResponseBody>, t: Throwable) {
                Log.e("D_Test", "페일!")
            }
        })
    }
}