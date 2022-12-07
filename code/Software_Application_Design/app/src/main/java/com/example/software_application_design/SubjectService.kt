package com.example.software_application_design

import com.google.gson.GsonBuilder
import okhttp3.MultipartBody
import okhttp3.OkHttpClient
import okhttp3.RequestBody
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*
import java.io.File

interface SubjectService {
    @GET("posts/get/")
    fun getSubject(
        @Query("title") title: String,
        @Query("text") text: String? = null,
        @Query("image") image: String? = null
    ) : Call<List<Subject>>

    @Multipart
    @POST("posts/")
    fun postSubject(
        @Part("ID") ID: RequestBody,
        @Part image: MultipartBody.Part
    ) : Call<ResponseBody>

    companion object{
        var BASE_URL = "https://9897-59-14-135-171.jp.ngrok.io/"
        private val gson =
            GsonBuilder()
                .setLenient()
                .create()
    }
}