package com.github.davidmoten.geo;

import com.google.common.collect.Sets;
import org.junit.Test;

import java.util.HashSet;

import static org.junit.Assert.*;

public class CoverageTest {
    @Test
    public void getRatio_TestT1() {
        HashSet<String> set =  new HashSet<String>();
        set.add("1");
        set.add("2");
        Coverage a = new Coverage(set,0.5);
        assertEquals(set, a.getHashes());
    }
    @Test
    public void getRatio_TestT2() {
        Coverage a = new Coverage(null,0.5);
        assertEquals(0.5, a.getRatio(), 0.5);
    }

    @Test
    public void getHashLength_Test() {
        Coverage a = new Coverage(Sets.<String> newHashSet("1234"), 123);
        assertEquals(4, a.getHashLength());
    }
    @Test
    public void getHashLength_TestT1() {
        Coverage a = new Coverage(Sets.<String> newHashSet(), 123);
        assertEquals(0, a.getHashLength());
    }
    @Test
    public void getHashLength_TestT2() {
        Coverage a = new Coverage(Sets.<String> newHashSet("56789"), 123);
        assertEquals(5, a.getHashLength());
    }

    @Test
    public void toStringTest(){
        Coverage a = new Coverage(Sets.<String> newHashSet("56789"), 123);
        assertEquals("Coverage [hashes=[56789], ratio=123.0]",a.toString());
    }
}