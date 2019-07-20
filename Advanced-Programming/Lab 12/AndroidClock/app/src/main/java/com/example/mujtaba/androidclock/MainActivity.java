package com.example.mujtaba.androidclock;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.List;
import java.util.Locale;
import java.util.TimeZone;

public class MainActivity extends AppCompatActivity {
    private Spinner timezone;
    private TextView time;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        time=(TextView) findViewById(R.id.time);
        timezone=(Spinner)findViewById(R.id.timezone);

        // Create a collection of all available countries
        List<String> countries = new ArrayList<String>();

        // Map ISO countries to custom country object
        String[] countryCodes = Locale.getISOCountries();
        for (String countryCode : countryCodes){

            Locale locale = new Locale("", countryCode);
            String name = locale.getDisplayCountry();

            countries.add(name);
        }

        ArrayAdapter<String> adp1 = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, countries);
        adp1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        timezone.setAdapter(adp1);
    }

    public void gettime(View v){
        String text = timezone.getSelectedItem().toString();

        Calendar cal = new GregorianCalendar(TimeZone.getTimeZone(text));
        int hour12 = cal.get(Calendar.HOUR); // 0..11
        int minutes = cal.get(Calendar.MINUTE); // 0..59
        int seconds = cal.get(Calendar.SECOND); // 0..59
        boolean am = cal.get(Calendar.AM_PM) == Calendar.AM;
        String pm;

        if (am==true)   pm="am";
        else   pm="pm";

        time.setText(Integer.toString(hour12)+":"+Integer.toString(minutes)+":"+Integer.toString(seconds)+":"+pm);
    }

}
