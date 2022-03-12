package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;

public class GeoHashTest {

    @Before
    public void setUp() throws Exception {

    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void encodeHash() {//4
        assertEquals("wsqqqm28s695",
                GeoHash.encodeHash(
                        25.033821717782278, 121.56459135583758));
        assertEquals("wsqqqm28",
                GeoHash.encodeHash(
                        25.033821717782278, 121.56459135583758,8));
        assertEquals("wsqqqm28s695",
                GeoHash.encodeHash(new LatLong(
                        25.033821717782278, 121.56459135583758)));
        assertEquals("wsqq",
                GeoHash.encodeHash(new LatLong(
                        25.033821717782278, 121.56459135583758),4));
    }
    @Test
    public void hasContains(){//1
        assertTrue(GeoHash.hashContains("wsqqqm28s",
                25.0338077545166, 121.564621925354));
        assertTrue(GeoHash.hashContains("wsqqqm28s",
                25.03385066986084, 121.564621925354));
        assertTrue(GeoHash.hashContains("wsqqqm28s",
                25.03385066986084, 121.56457901000977));
        assertTrue(GeoHash.hashContains("wsqqqm28s",
                25.0338077545166, 121.56457901000977));
        assertFalse(GeoHash.hashContains("wsqqqm28s",
                25.0338077545165, 121.564621925354));
        assertFalse(GeoHash.hashContains("wsqqqm28s",
                25.03385066986085, 121.564621925354));
        assertFalse(GeoHash.hashContains("wsqqqm28s",
                25.03385066986084, 122.56457901000977));
        assertFalse(GeoHash.hashContains("wsqqqm28s",
                25.0338077545166, 120.56457901000977));
    }
    @Test
    public void adjacentHash(){//2
        assertEquals("wsqqhp8hk1mp",
                GeoHash.adjacentHash("wsqqhp8hk1mn",Direction.TOP));
        assertEquals("wsqqhp8hk1t1",
                GeoHash.adjacentHash("wsqqhp8hk1mn",Direction.TOP,3));
    }
    @Test
    public void right(){
        assertEquals("wsqqhjwyuveh",
                GeoHash.right("wsqqhjwyuvdu"));
    }
    @Test
    public void bottom(){
        assertEquals("wsqqhjwyuvdg",
                GeoHash.bottom("wsqqhjwyuvdu"));
    }
    @Test
    public void decodeHash(){
        LatLong latLong = GeoHash.decodeHash("wsqqhjwyuvdu");
        assertEquals(24.99233888,latLong.getLat(),0.001);
        assertEquals(121.47432117,latLong.getLon(),0.001);
    }

}