package com.printnanny.api.rust;

/*
 * Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
 * Copyright 2018 SmartBear Software
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import org.openapitools.codegen.CodegenConstants;
import com.printnanny.api.rust.RustClientGenerator;
import org.testng.Assert;
import org.testng.annotations.Test;

public class RustClientGeneratorTest {

  @Test
  public void testInitialConfigValues() throws Exception {
    final RustClientGenerator codegen = new RustClientGenerator();
    codegen.processOpts();

    Assert.assertEquals(codegen.additionalProperties().get(CodegenConstants.HIDE_GENERATION_TIMESTAMP), Boolean.TRUE);
    Assert.assertEquals(codegen.isHideGenerationTimestamp(), true);
  }

  @Test
  public void testSettersForConfigValues() throws Exception {
    final RustClientGenerator codegen = new RustClientGenerator();
    codegen.setHideGenerationTimestamp(false);
    codegen.processOpts();

    Assert.assertEquals(codegen.additionalProperties().get(CodegenConstants.HIDE_GENERATION_TIMESTAMP), Boolean.FALSE);
    Assert.assertEquals(codegen.isHideGenerationTimestamp(), false);
  }

  @Test
  public void testAdditionalPropertiesPutForConfigValues() throws Exception {
    final RustClientGenerator codegen = new RustClientGenerator();
    codegen.additionalProperties().put(CodegenConstants.HIDE_GENERATION_TIMESTAMP, false);
    codegen.processOpts();

    Assert.assertEquals(codegen.additionalProperties().get(CodegenConstants.HIDE_GENERATION_TIMESTAMP), Boolean.FALSE);
    Assert.assertEquals(codegen.isHideGenerationTimestamp(), false);
  }

}