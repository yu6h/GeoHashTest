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
    public void encodeHashT1() {//4
        assertEquals("wkw946psk8ec",
                GeoHash.encodeHash(
                        25.5, 110.5));
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashT2() {//4
        GeoHash.encodeHash(
                -91, 110.5);
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashT3() {//4
        GeoHash.encodeHash(
                25.5, 181);
    }
    @Test
    public void encodeHashWithLatLoneAsParameterT1() {//4
        assertEquals("eux314pu629c",
                GeoHash.encodeHash(new LatLong(
                        25.5, -1)));
    }
    @Test
    public void encodeHashWithLatLoneAsParameterT2() {//4
        assertEquals("sh81040h2081",
                GeoHash.encodeHash(new LatLong(
                        25.5, 0)));

    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWithLatLoneAsParameterT3(){//4
                GeoHash.encodeHash(new LatLong(
                        -91, 200));
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWithLatLoneAsParameterT4(){//4
        GeoHash.encodeHash(new LatLong(
                91, 20));
    }
    @Test
    public void encodeHashWithLatLoneAndLengthAsParameterT1() {//4
        assertEquals("eux31",
                GeoHash.encodeHash(new LatLong(
                        25.5, -1),5));
    }
    @Test
    public void encodeHashWithLatLoneAndLengthAsParameterT3() {
        assertEquals("sh81040h20",
                GeoHash.encodeHash(new LatLong(
                        25.5, 0),10));
    }

    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWithLatLoneAndLengthAsParameterT5() {
                GeoHash.encodeHash(new LatLong(
                        -91, -150),10);
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWithLatLoneAndLengthAsParameterT7() {
        GeoHash.encodeHash(new LatLong(
                -91, 150),10);
    }
    @Test
    public void encodeHashWith3ParametersT1() {
        assertEquals("n",
                GeoHash.encodeHash(
                        -60.5, 121.8,1));
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWith3ParametersT2() {
        GeoHash.encodeHash(-60.5, 121.8,0);
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWith3ParametersT3() {//4
        GeoHash.encodeHash(-60.5, -181,1);
    }
    @Test(expected = IllegalArgumentException.class)
    public void encodeHashWith3ParametersT4() {//4
        GeoHash.encodeHash(-91, 121.8,1);
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
    @Test(expected = NullPointerException.class)
    public void hasContainsT1(){//1
        assertTrue(GeoHash.hashContains(null,
                25.5, 122.2));
    }
    @Test(expected = NullPointerException.class)
    public void hasContainsT2(){//1
        assertTrue(GeoHash.hashContains(null,
                25.5, -181));
    }
    @Test(expected = NullPointerException.class)
    public void hasContainsT3(){//1
        assertTrue(GeoHash.hashContains(null,
                25.5, 122));
    }
    @Test
    public void hasContainsT4(){//1
        assertTrue(GeoHash.hashContains("wsqqqm28",
                25.03380775, 121.56457901));
    }
    @Test
    public void adjacentHash(){//2
        assertEquals("wsqqhp8hk1mp",
                GeoHash.adjacentHash("wsqqhp8hk1mn",Direction.TOP));
        assertEquals("wsqqhp8hk1t1",
                GeoHash.adjacentHash("wsqqhp8hk1mn",Direction.TOP,3));
    }
    @Test(expected = IllegalArgumentException.class)
    public void adjacentHashT1(){//2
                GeoHash.adjacentHash(null,Direction.BOTTOM);
    }
    @Test
    public void adjacentHashT5(){//2
        assertEquals("yenm",
        GeoHash.adjacentHash("yenq",Direction.BOTTOM));
    }
    @Test
    public void adjacentHashT6(){//2
        assertEquals("1338",
                GeoHash.adjacentHash("131x",Direction.TOP));
    }
    @Test
    public void adjacentHashT7(){//2
        assertEquals("h1gq",
                GeoHash.adjacentHash("h1gw",Direction.LEFT));
    }
    @Test
    public void adjacentHashT8(){//2
        assertEquals("23y2",
                GeoHash.adjacentHash("23y0",Direction.RIGHT));
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

    @Test
    public void hashLengthToCoverBoundingBox(){
        assertEquals(1,GeoHash.
                hashLengthToCoverBoundingBox(24.67693180092837, 121.73868842362948,
                        22.09087140332405, 120.75488854089994));
        assertEquals(0,GeoHash.
                hashLengthToCoverBoundingBox(36.633950257465244, 138.20176404334265,
                        -1.2383111850902806, 103.60559538049397));
        assertEquals(3,GeoHash.
                hashLengthToCoverBoundingBox(29.240501036359017, 107.95600702691077,
                        29.230257104690256, 107.92737197784561));
    }
    @Test
    public void neighbours(){
        List<String> list = java.util.Arrays
                .asList("wsqqhjwyuvds", "wsqqhjwyuveh",
                        "wsqqhjwyuvdv", "wsqqhjwyuvdg",
                        "wsqqhjwyuvdt", "wsqqhjwyuvde",
                        "wsqqhjwyuvej", "wsqqhjwyuve5");
        assertTrue(list.equals(GeoHash.neighbours("wsqqhjwyuvdu")));
    }
}