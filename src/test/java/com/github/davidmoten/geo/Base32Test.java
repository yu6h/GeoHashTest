package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Base32Test {

    @Before
    public void setUp() throws Exception {

    }

    @After
    public void tearDown() throws Exception {

    }

    @Test
    public void EncodeBase32WithTwoParameters() throws Exception {
        String encode = Base32.encodeBase32(75324, 4);
        assertEquals("29jw", encode);
    }
    @Test
    public void EncodeBase32() throws Exception {
        String encode = Base32.encodeBase32(15324);
        assertEquals("000000000fyw", encode);
    }
}


