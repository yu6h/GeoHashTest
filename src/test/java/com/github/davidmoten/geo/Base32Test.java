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
    @Test
    public void EncodeBase32T1() throws Exception {
        String encode = Base32.encodeBase32(-32);
        assertEquals("-000000000010", encode);
    }
    @Test
    public void EncodeBase32T2() throws Exception {
        String encode = Base32.encodeBase32(-15);
        assertEquals("-00000000000g", encode);
    }
    @Test
    public void EncodeBase32T3() throws Exception {
        String encode = Base32.encodeBase32(0);
        assertEquals("000000000000", encode);
    }
    @Test
    public void EncodeBase32WithTwoParametersT1() throws Exception {
        String encode = Base32.encodeBase32(-33, 5);
        assertEquals("-00011", encode);
    }
    @Test
    public void EncodeBase32WithTwoParametersT4() throws Exception {
        String encode = Base32.encodeBase32(-15, 5);
        assertEquals("-0000g", encode);
    }
    @Test
    public void EncodeBase32WithTwoParametersT7() throws Exception {
        String encode = Base32.encodeBase32(1, 4);
        assertEquals("0001", encode);
    }

    @Test
    public void testDecodeBase32(){
        assertEquals(75324,Base32.decodeBase32("29jw"));
    }
}


