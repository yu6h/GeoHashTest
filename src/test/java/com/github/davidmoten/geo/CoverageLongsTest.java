package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CoverageLongsTest {
    private CoverageLongs coverageLongs;
    @Before
    public void setUp() throws Exception {

    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getHashes() {
    }

    @Test
    public void getRatio() {
    }

    @Test
    public void getHashLengthT1() {
        coverageLongs = new CoverageLongs(new long[] {}, 0, 1.0);
        coverageLongs.getHashLength();
        assertEquals(0,coverageLongs.getHashLength());
        System.out.println(coverageLongs);
    }
    @Test
    public void getHashLengthT2() {
        coverageLongs = new CoverageLongs(new long[] {100,10000}, 2, 1.0);
        coverageLongs.getHashLength();
        assertEquals(4,coverageLongs.getHashLength());
        System.out.println(coverageLongs);
    }

    @Test
    public void getCount() {
    }
}