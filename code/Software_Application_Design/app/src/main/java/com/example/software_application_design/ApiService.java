package com.example.software_application_design;



import java.util.HashMap;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.Field;
import retrofit2.http.FieldMap;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface ApiService {
    public static final String API_URL = "https://428c-59-14-135-171.jp.ngrok.io/";
    @GET("posts")
    Call<ResponseBody> get_Test(@Query("format") String json);

    @FormUrlEncoded
    @POST("posts")
    Call<Json_Test> post_Test(@FieldMap HashMap<String, Object> param);

    @FormUrlEncoded
    @POST("posts")
    Call<ResponseBody> post_Test2(@Field("email") String test);

    @FormUrlEncoded
    @PATCH("posts/{pk}/")
    Call<ResponseBody> patch_Test(@Path("pk") int pk, @Query("format") String json, @Field("email") String test);

    @DELETE("posts/{pk}/")
    Call<ResponseBody> delete_Patch_Test(@Path("pk") int pk, @Query("format") String json);

    @POST("posts")
    Call<Json_Test_Java> post_json_test_java(@Query("format") String json, @Body Json_Test_Java json_test_java);
}
