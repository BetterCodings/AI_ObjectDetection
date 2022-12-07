package com.example.software_application_design

import com.google.gson.annotations.SerializedName
import java.io.File

data class Subject(
    @SerializedName("ID")
    val ID: String? = null,
    @SerializedName("image")
    val image: File? = null,
)