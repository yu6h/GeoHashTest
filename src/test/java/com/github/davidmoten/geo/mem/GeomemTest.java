package com.github.davidmoten.geo.mem;

import com.google.common.base.Predicate;
import com.google.common.collect.Lists;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.List;
import com.google.common.base.Optional;

import static org.junit.Assert.*;

public class GeomemTest {
    private Geomem<Integer, String> geomem;
    private Geomem<String, String> geomemForRegionFilter;
    private Predicate<Info<String, String>> predicateForRegionFilter;
    private static final double topLeftLat = 45;
    private static final double topLeftLong = 90;
    private static final double bottomRightLat = 0;
    private static final double bottomRightLong = 135;
    @Before
    public void setUp() throws Exception {
        geomem = new Geomem<Integer, String>();
        geomemForRegionFilter = new Geomem<String, String>();
        predicateForRegionFilter = geomemForRegionFilter.createRegionFilter(
                topLeftLat, topLeftLong, bottomRightLat, bottomRightLong);
    }

    @After
    public void tearDown() throws Exception {
    }
    @Test
    public void testRegionFilterT1(){
        assertFalse(predicateForRegionFilter.apply(new Info<String, String>(bottomRightLat-1, bottomRightLong, 100, "A", Optional.of("A"))));
    }
    @Test
    public void testRegionFilterT2(){
        assertFalse(predicateForRegionFilter.apply(new Info<String, String>(topLeftLat, bottomRightLong, 100, "A", Optional.of("A"))));
    }
    @Test
    public void testRegionFilterT3(){
        assertFalse(predicateForRegionFilter.apply(new Info<String, String>(bottomRightLat, topLeftLong, 100, "A", Optional.of("A"))));
    }
    @Test
    public void testRegionFilterT4(){
        assertFalse(predicateForRegionFilter.apply(new Info<String, String>(bottomRightLat, bottomRightLong+1, 100, "A", Optional.of("A"))));
    }
    @Test
    public void testRegionFilterT5(){
        assertTrue(predicateForRegionFilter.apply(new Info<String, String>(bottomRightLat, bottomRightLong, 100, "A", Optional.of("A"))));
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