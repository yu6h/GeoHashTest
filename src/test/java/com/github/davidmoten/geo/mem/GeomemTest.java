package com.github.davidmoten.geo.mem;

import org.junit.Test;

import java.util.Optional;

import static org.junit.Assert.*;

public class GeomemTest {
    @Test
    public void addWith4ParametersT1(){
        Geomem<Integer, String> geomem = new Geomem<Integer, String>();
        geomem.add(25.5,122,1,1);
    }
    @Test(expected = IllegalArgumentException.class)
    public void addWith4ParametersT2(){
        Geomem<Integer, String> geomem = new Geomem<Integer, String>();
        geomem.add(-91,122,1,1);
    }
    @Test
    public void addWith4ParametersT3(){
        Geomem<Integer, String> geomem = new Geomem<Integer, String>();
        geomem.add(60,188,1,1);
    }
}