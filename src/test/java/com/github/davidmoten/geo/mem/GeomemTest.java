package com.github.davidmoten.geo.mem;

import com.google.common.collect.Lists;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.List;
import java.util.Optional;

import static org.junit.Assert.*;

public class GeomemTest {
    private Geomem<Integer, String> geomem;
    @Before
    public void setUp() throws Exception {
        geomem = new Geomem<Integer, String>();
    }

    @After
    public void tearDown() throws Exception {
    }
    @Test
    public void find_by_T1(){
        Geomem<String, String> g = new Geomem<String, String>();

        Iterable<Info<String,String>> x =  g.find(0,0, 0, 0, 0, 0);
        List<Info<String, String>> list = Lists.newArrayList(x);
        assertTrue(list.isEmpty());
    }

    @Test
    public void addWith4ParametersT1(){
        geomem.add(25.5,122,1,1);
    }
    @Test(expected = IllegalArgumentException.class)
    public void addWith4ParametersT2(){
        geomem.add(-91,122,1,1);
    }
    @Test
    public void addWith4ParametersT3(){
        geomem.add(60,188,1,1);
    }
}