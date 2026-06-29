```diff
────── Python AST
ModuleJsonOp  ← []
├── DefineStructOp  ← []
├── DefineStructOp  ← []
├── DefineStructOp  ← []
└── FunctionOp('xdsl_main')  ← []
    ├── Init args
    │   ├── Factory.from_val  ← ValPtr(addr, Ptr(Struct('simu')))
    │   │   │       - type = Ptr(Struct('simu'))
    │   │   │       - value = ValSSA()
    │   │   │       - builder = <Builder ... >
    │   │   └── ValPtr.init_from  ← ValPtr(addr, Ptr(Struct('simu')))
    │   │       │       - type = Ptr(Struct('simu'))
    │   │       │       - source = ValSSA()
    │   │       │       - builder = <Builder ... >
    │   │       └── ValPtr._store([], ValSSA())  ← None
    │   └── Factory.from_val  ← ValScalar(addr, Scalar(i64))
    │       │       - type = Scalar(i64)
    │       │       - value = ValSSA()
    │       │       - builder = <Builder ... >
    │       └── ValScalar.init_from  ← ValScalar(addr, Scalar(i64))
    │           │       - type = Scalar(i64)
    │           │       - source = ValSSA()
    │           │       - builder = <Builder ... >
    │           └── ValScalar._store([], ValSSA())  ← None
    └── CodegenBlock  ← (<Block ... >, [ValScalar(addr, Scalar(i64))])
        │       - content = [VarOp]
        │       - block = <Block ... >
        └── VarOp('simuReference', ['*', 'positions', '*', 'coords', '*', 3, 'y'])  ← [ValScalar(addr, Scalar(i64))]
            └── ValPtr._load(['*', 'positions', '*', 'coords', '*', <OpResult name_hint: const3.index, index: 0, operation: arith.constant, uses: 0>, 'y'])  ← ValScalar(addr, Scalar(i64))
                ├── Factory.from_val  ← ValStruct(addr, Struct('simu'))
                │   │       - type = Struct('simu')
                │   │       - value = ValSSA()
                │   │       - builder = <Builder ... >
                │   └── ValStruct.init_from  ← ValStruct(addr, Struct('simu'))
                │       │       - type = Struct('simu')
                │       │       - source = ValSSA()
                │       │       - builder = <Builder ... >
                └── ValStruct._load(['positions', '*', 'coords', '*', <OpResult name_hint: const3.index, index: 0, operation: arith.constant, uses: 0>, 'y'])  ← ValScalar(addr, Scalar(i64))
                    ├── Factory.from_val  ← ValPtr(addr, Ptr(Struct('noeuds')))
                    │   │       - type = Ptr(Struct('noeuds'))
                    │   │       - value = ValSSA()
                    │   │       - builder = <Builder ... >
                    │   └── ValPtr.init_from  ← ValPtr(addr, Ptr(Struct('noeuds')))
                    │       │       - type = Ptr(Struct('noeuds'))
                    │       │       - source = ValSSA()
                    │       │       - builder = <Builder ... >
                    │       └── ValPtr._store([], ValSSA())  ← None
                    └── ValPtr._load(['*', 'coords', '*', <OpResult name_hint: const3.index, index: 0, operation: arith.constant, uses: 0>, 'y'])  ← ValScalar(addr, Scalar(i64))
                        ├── Factory.from_val  ← ValStruct(addr, Struct('noeuds'))
                        │   │       - type = Struct('noeuds')
                        │   │       - value = ValSSA()
                        │   │       - builder = <Builder ... >
                        │   └── ValStruct.init_from  ← ValStruct(addr, Struct('noeuds'))
                        │       │       - type = Struct('noeuds')
                        │       │       - source = ValSSA()
                        │       │       - builder = <Builder ... >
                        └── ValStruct._load(['coords', '*', <OpResult name_hint: const3.index, index: 0, operation: arith.constant, uses: 0>, 'y'])  ← ValScalar(addr, Scalar(i64))
                            ├── Factory.from_val  ← ValPtr(addr, Ptr(Memref(dims=[5], base=Struct('xyz'))))
                            │   │       - type = Ptr(Memref(dims=[5], base=Struct('xyz')))
                            │   │       - value = ValSSA()
                            │   │       - builder = <Builder ... >
                            │   └── ValPtr.init_from  ← ValPtr(addr, Ptr(Memref(dims=[5], base=Struct('xyz'))))
                            │       │       - type = Ptr(Memref(dims=[5], base=Struct('xyz')))
                            │       │       - source = ValSSA()
                            │       │       - builder = <Builder ... >
                            │       └── ValPtr._store([], ValSSA())  ← None
                            └── ValPtr._load(['*', <OpResult name_hint: const3.index, index: 0, operation: arith.constant, uses: 0>, 'y'])  ← ValScalar(addr, Scalar(i64))
                                ├── Factory.from_val  ← ValMemref(addr, Memref(dims=[5], base=Struct('xyz')))
                                │   │       - type = Memref(dims=[5], base=Struct('xyz'))
                                │   │       - value = ValSSA()
                                │   │       - builder = <Builder ... >
                                │   └── ValMemref.init_from  ← ValMemref(addr, Memref(dims=[5], base=Struct('xyz')))
                                │       │       - type = Memref(dims=[5], base=Struct('xyz'))
                                │       │       - source = ValSSA()
                                │       │       - builder = <Builder ... >
                                └── ValMemref._load([<OpResult name_hint: const3.index, index: 0, operation: arith.constant, uses: 0>, 'y'])  ← ValScalar(addr, Scalar(i64))
                                    ├── Factory.from_SSA  ← ValStruct(addr, Struct('xyz'))
                                    │   │       - type = Struct('xyz')
                                    │   │       - addr = <OpResult name_hint: None, index: 0, operation: memref.subview, uses: 0>
                                    │   │       - builder = <Builder ... >
                                    │   └── Factory.from_val  ← ValStruct(addr, Struct('xyz'))
                                    │       │       - type = Struct('xyz')
                                    │       │       - value = ValSSA()
                                    │       │       - builder = <Builder ... >
                                    │       └── ValStruct.init_from  ← ValStruct(addr, Struct('xyz'))
                                    │           │       - type = Struct('xyz')
                                    │           │       - source = ValSSA()
                                    │           │       - builder = <Builder ... >
                                    └── ValStruct._load(['y'])  ← ValScalar(addr, Scalar(i64))
                                        └── Factory.from_val  ← ValScalar(addr, Scalar(i64))
                                            │       - type = Scalar(i64)
                                            │       - value = ValSSA()
                                            │       - builder = <Builder ... >
                                            └── ValScalar.init_from  ← ValScalar(addr, Scalar(i64))
                                                │       - type = Scalar(i64)
                                                │       - source = ValSSA()
                                                │       - builder = <Builder ... >
                                                └── ValScalar._store([], ValSSA())  ← None

────── xDSL
builtin.module {
  func.func @xdsl_main(%simuReferenceArg: i64, %iArg: i64) -> i64 attributes {llvm.emit_c_interface} {
    %const8.index = arith.constant 8 : index
    %const1.index = arith.constant 1 : index
    %const24.index = arith.constant 24 : index
    %const0.index = arith.constant 0 : index
    %const3.index = arith.constant 3 : index
    %0 = memref.alloca() : memref<i64>
    memref.store %simuReferenceArg, %0[] : memref<i64>
    %1 = memref.alloca() : memref<i64>
    memref.store %iArg, %1[] : memref<i64>
    %2 = memref.load %0[] : memref<i64>
    %3 = llvm.inttoptr %2 : i64 to !llvm.ptr
    %4 = builtin.unrealized_conversion_cast %3 : !llvm.ptr to !ptr_xdsl.ptr
    %5 = ptr_xdsl.from_ptr %4 : !ptr_xdsl.ptr -> memref<32xi8>
    %6 = memref.view %5[%const0.index][] : memref<32xi8> to memref<i64>
    %7 = memref.alloca() : memref<i64>
    %8 = memref.load %6[] : memref<i64>
    memref.store %8, %7[] : memref<i64>
    %9 = memref.load %7[] : memref<i64>
    %10 = llvm.inttoptr %9 : i64 to !llvm.ptr
    %11 = builtin.unrealized_conversion_cast %10 : !llvm.ptr to !ptr_xdsl.ptr
    %12 = ptr_xdsl.from_ptr %11 : !ptr_xdsl.ptr -> memref<16xi8>
    %13 = memref.view %12[%const0.index][] : memref<16xi8> to memref<i64>
    %14 = memref.alloca() : memref<i64>
    %15 = memref.load %13[] : memref<i64>
    memref.store %15, %14[] : memref<i64>
    %16 = memref.load %14[] : memref<i64>
    %17 = llvm.inttoptr %16 : i64 to !llvm.ptr
    %18 = builtin.unrealized_conversion_cast %17 : !llvm.ptr to !ptr_xdsl.ptr
    %19 = ptr_xdsl.from_ptr %18 : !ptr_xdsl.ptr -> memref<120xi8>
    %20 = memref.subview %19[%const3.index] [%const24.index] [%const1.index] : memref<120xi8> to memref<24xi8>
    %21 = memref.view %20[%const8.index][] : memref<24xi8> to memref<i64>
    %22 = memref.alloca() : memref<i64>
    %23 = memref.load %21[] : memref<i64>
    memref.store %23, %22[] : memref<i64>
    %24 = memref.load %22[] : memref<i64>
    func.return %24 : i64
  }
}


────── xDSL afte ConvertMemRefToPtr passe
--- before                                                                                                                                                                                   
+++ xDSL afte ConvertMemRefToPtr passe                                                                                                                                                       
@@ -1,40 +1,69 @@                                                                                                                                                                            
 builtin.module {                                                                                                                                                                            
   func.func @xdsl_main(%simuReferenceArg: i64, %iArg: i64) -> i64 attributes {llvm.emit_c_interface} {                                                                                      
     %const8.index = arith.constant 8 : index                                                                                                                                                
-    %const1.index = arith.constant 1 : index                                                                                                                                                
-    %const24.index = arith.constant 24 : index                                                                                                                                              
     %const0.index = arith.constant 0 : index                                                                                                                                                
     %const3.index = arith.constant 3 : index                                                                                                                                                
-    %0 = memref.alloca() : memref<i64>                                                                                                                                                      
-    memref.store %simuReferenceArg, %0[] : memref<i64>                                                                                                                                      
-    %1 = memref.alloca() : memref<i64>                                                                                                                                                      
-    memref.store %iArg, %1[] : memref<i64>                                                                                                                                                  
-    %2 = memref.load %0[] : memref<i64>                                                                                                                                                     
-    %3 = llvm.inttoptr %2 : i64 to !llvm.ptr                                                                                                                                                
-    %4 = builtin.unrealized_conversion_cast %3 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                 
-    %5 = ptr_xdsl.from_ptr %4 : !ptr_xdsl.ptr -> memref<32xi8>                                                                                                                              
-    %6 = memref.view %5[%const0.index][] : memref<32xi8> to memref<i64>                                                                                                                     
-    %7 = memref.alloca() : memref<i64>                                                                                                                                                      
-    %8 = memref.load %6[] : memref<i64>                                                                                                                                                     
-    memref.store %8, %7[] : memref<i64>                                                                                                                                                     
-    %9 = memref.load %7[] : memref<i64>                                                                                                                                                     
+    %c1 = arith.constant 1 : i32                                                                                                                                                            
+    %0 = llvm.alloca %c1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                  
+    %1 = builtin.unrealized_conversion_cast %0 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                 
+    %2 = ptr_xdsl.from_ptr %1 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                                
+    %3 = ptr_xdsl.to_ptr %2 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                  
+    ptr_xdsl.store %simuReferenceArg, %3 : i64, !ptr_xdsl.ptr                                                                                                                               
+    %c1_1 = arith.constant 1 : i32                                                                                                                                                          
+    %4 = llvm.alloca %c1_1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
+    %5 = builtin.unrealized_conversion_cast %4 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                 
+    %6 = ptr_xdsl.from_ptr %5 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                                
+    %7 = ptr_xdsl.to_ptr %6 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                  
+    ptr_xdsl.store %iArg, %7 : i64, !ptr_xdsl.ptr                                                                                                                                           
+    %8 = ptr_xdsl.to_ptr %2 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                  
+    %9 = ptr_xdsl.load %8 : !ptr_xdsl.ptr -> i64                                                                                                                                            
     %10 = llvm.inttoptr %9 : i64 to !llvm.ptr                                                                                                                                               
     %11 = builtin.unrealized_conversion_cast %10 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %12 = ptr_xdsl.from_ptr %11 : !ptr_xdsl.ptr -> memref<16xi8>                                                                                                                            
-    %13 = memref.view %12[%const0.index][] : memref<16xi8> to memref<i64>                                                                                                                   
-    %14 = memref.alloca() : memref<i64>                                                                                                                                                     
-    %15 = memref.load %13[] : memref<i64>                                                                                                                                                   
-    memref.store %15, %14[] : memref<i64>                                                                                                                                                   
-    %16 = memref.load %14[] : memref<i64>                                                                                                                                                   
-    %17 = llvm.inttoptr %16 : i64 to !llvm.ptr                                                                                                                                              
-    %18 = builtin.unrealized_conversion_cast %17 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %19 = ptr_xdsl.from_ptr %18 : !ptr_xdsl.ptr -> memref<120xi8>                                                                                                                           
-    %20 = memref.subview %19[%const3.index] [%const24.index] [%const1.index] : memref<120xi8> to memref<24xi8>                                                                              
-    %21 = memref.view %20[%const8.index][] : memref<24xi8> to memref<i64>                                                                                                                   
-    %22 = memref.alloca() : memref<i64>                                                                                                                                                     
-    %23 = memref.load %21[] : memref<i64>                                                                                                                                                   
-    memref.store %23, %22[] : memref<i64>                                                                                                                                                   
-    %24 = memref.load %22[] : memref<i64>                                                                                                                                                   
-    func.return %24 : i64                                                                                                                                                                   
+    %12 = ptr_xdsl.from_ptr %11 : !ptr_xdsl.ptr -> memref<32xi8>                                                                                                                            
+    %13 = memref.view %12[%const0.index][] : memref<32xi8> to memref<i64>                                                                                                                   
+    %c1_2 = arith.constant 1 : i32                                                                                                                                                          
+    %14 = llvm.alloca %c1_2 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
+    %15 = builtin.unrealized_conversion_cast %14 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
+    %16 = ptr_xdsl.from_ptr %15 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                              
+    %17 = ptr_xdsl.to_ptr %13 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    %18 = ptr_xdsl.load %17 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    %19 = ptr_xdsl.to_ptr %16 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    ptr_xdsl.store %18, %19 : i64, !ptr_xdsl.ptr                                                                                                                                            
+    %20 = ptr_xdsl.to_ptr %16 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    %21 = ptr_xdsl.load %20 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    %22 = llvm.inttoptr %21 : i64 to !llvm.ptr                                                                                                                                              
+    %23 = builtin.unrealized_conversion_cast %22 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
+    %24 = ptr_xdsl.from_ptr %23 : !ptr_xdsl.ptr -> memref<16xi8>                                                                                                                            
+    %25 = memref.view %24[%const0.index][] : memref<16xi8> to memref<i64>                                                                                                                   
+    %c1_3 = arith.constant 1 : i32                                                                                                                                                          
+    %26 = llvm.alloca %c1_3 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
+    %27 = builtin.unrealized_conversion_cast %26 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
+    %28 = ptr_xdsl.from_ptr %27 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                              
+    %29 = ptr_xdsl.to_ptr %25 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    %30 = ptr_xdsl.load %29 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    %31 = ptr_xdsl.to_ptr %28 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    ptr_xdsl.store %30, %31 : i64, !ptr_xdsl.ptr                                                                                                                                            
+    %32 = ptr_xdsl.to_ptr %28 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    %33 = ptr_xdsl.load %32 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    %34 = llvm.inttoptr %33 : i64 to !llvm.ptr                                                                                                                                              
+    %35 = builtin.unrealized_conversion_cast %34 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
+    %36 = ptr_xdsl.from_ptr %35 : !ptr_xdsl.ptr -> memref<120xi8>                                                                                                                           
+    %37 = ptr_xdsl.to_ptr %36 : memref<120xi8> -> !ptr_xdsl.ptr                                                                                                                             
+    %bytes_per_element = ptr_xdsl.type_offset i8 : index                                                                                                                                    
+    %scaled_pointer_offset = arith.muli %const3.index, %bytes_per_element : index                                                                                                           
+    %offset_pointer = ptr_xdsl.ptradd %37, %scaled_pointer_offset : (!ptr_xdsl.ptr, index) -> !ptr_xdsl.ptr                                                                                 
+    %38 = ptr_xdsl.from_ptr %offset_pointer : !ptr_xdsl.ptr -> memref<24xi8>                                                                                                                
+    %39 = memref.view %38[%const8.index][] : memref<24xi8> to memref<i64>                                                                                                                   
+    %c1_4 = arith.constant 1 : i32                                                                                                                                                          
+    %40 = llvm.alloca %c1_4 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
+    %41 = builtin.unrealized_conversion_cast %40 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
+    %42 = ptr_xdsl.from_ptr %41 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                              
+    %43 = ptr_xdsl.to_ptr %39 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    %44 = ptr_xdsl.load %43 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    %45 = ptr_xdsl.to_ptr %42 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    ptr_xdsl.store %44, %45 : i64, !ptr_xdsl.ptr                                                                                                                                            
+    %46 = ptr_xdsl.to_ptr %42 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
+    %47 = ptr_xdsl.load %46 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    func.return %47 : i64                                                                                                                                                                   
   }                                                                                                                                                                                         
 }                                                                                                                                                                                           


────── xDSL afte ConvertPtrTypeOffsetsPass passe
--- before                                                                                                                                                                                   
+++ xDSL afte ConvertPtrTypeOffsetsPass passe                                                                                                                                                
@@ -49,7 +49,7 @@                                                                                                                                                                            
     %35 = builtin.unrealized_conversion_cast %34 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
     %36 = ptr_xdsl.from_ptr %35 : !ptr_xdsl.ptr -> memref<120xi8>                                                                                                                           
     %37 = ptr_xdsl.to_ptr %36 : memref<120xi8> -> !ptr_xdsl.ptr                                                                                                                             
-    %bytes_per_element = ptr_xdsl.type_offset i8 : index                                                                                                                                    
+    %bytes_per_element = arith.constant 1 : index                                                                                                                                           
     %scaled_pointer_offset = arith.muli %const3.index, %bytes_per_element : index                                                                                                           
     %offset_pointer = ptr_xdsl.ptradd %37, %scaled_pointer_offset : (!ptr_xdsl.ptr, index) -> !ptr_xdsl.ptr                                                                                 
     %38 = ptr_xdsl.from_ptr %offset_pointer : !ptr_xdsl.ptr -> memref<24xi8>                                                                                                                

/home/lmx/git/xdsl-json/xdsl/xdsl/transforms/reconcile_unrealized_casts.py:75: UserWarning: Unable to remove cast UnrealizedConversionCastOp(%0 = builtin.unrealized_conversion_cast %1 : !llvm.ptr to !ptr_xdsl.ptr) because it is not unifiable with its uses
  warn(

────── xDSL afte ReconcileUnrealizedCastsPass passe
builtin.module {                                                                                                                                                                             
  func.func @xdsl_main(%simuReferenceArg: i64, %iArg: i64) -> i64 attributes {llvm.emit_c_interface} {                                                                                       
    %const8.index = arith.constant 8 : index                                                                                                                                                 
    %const0.index = arith.constant 0 : index                                                                                                                                                 
    %const3.index = arith.constant 3 : index                                                                                                                                                 
    %c1 = arith.constant 1 : i32                                                                                                                                                             
    %0 = llvm.alloca %c1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                   
    %1 = builtin.unrealized_conversion_cast %0 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                  
    %2 = ptr_xdsl.from_ptr %1 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                                 
    %3 = ptr_xdsl.to_ptr %2 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                   
    ptr_xdsl.store %simuReferenceArg, %3 : i64, !ptr_xdsl.ptr                                                                                                                                
    %c1_1 = arith.constant 1 : i32                                                                                                                                                           
    %4 = llvm.alloca %c1_1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                 
    %5 = builtin.unrealized_conversion_cast %4 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                  
    %6 = ptr_xdsl.from_ptr %5 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                                 
    %7 = ptr_xdsl.to_ptr %6 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                   
    ptr_xdsl.store %iArg, %7 : i64, !ptr_xdsl.ptr                                                                                                                                            
    %8 = ptr_xdsl.to_ptr %2 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                   
    %9 = ptr_xdsl.load %8 : !ptr_xdsl.ptr -> i64                                                                                                                                             
    %10 = llvm.inttoptr %9 : i64 to !llvm.ptr                                                                                                                                                
    %11 = builtin.unrealized_conversion_cast %10 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                
    %12 = ptr_xdsl.from_ptr %11 : !ptr_xdsl.ptr -> memref<32xi8>                                                                                                                             
    %13 = memref.view %12[%const0.index][] : memref<32xi8> to memref<i64>                                                                                                                    
    %c1_2 = arith.constant 1 : i32                                                                                                                                                           
    %14 = llvm.alloca %c1_2 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
    %15 = builtin.unrealized_conversion_cast %14 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                
    %16 = ptr_xdsl.from_ptr %15 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                               
    %17 = ptr_xdsl.to_ptr %13 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    %18 = ptr_xdsl.load %17 : !ptr_xdsl.ptr -> i64                                                                                                                                           
    %19 = ptr_xdsl.to_ptr %16 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    ptr_xdsl.store %18, %19 : i64, !ptr_xdsl.ptr                                                                                                                                             
    %20 = ptr_xdsl.to_ptr %16 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    %21 = ptr_xdsl.load %20 : !ptr_xdsl.ptr -> i64                                                                                                                                           
    %22 = llvm.inttoptr %21 : i64 to !llvm.ptr                                                                                                                                               
    %23 = builtin.unrealized_conversion_cast %22 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                
    %24 = ptr_xdsl.from_ptr %23 : !ptr_xdsl.ptr -> memref<16xi8>                                                                                                                             
    %25 = memref.view %24[%const0.index][] : memref<16xi8> to memref<i64>                                                                                                                    
    %c1_3 = arith.constant 1 : i32                                                                                                                                                           
    %26 = llvm.alloca %c1_3 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
    %27 = builtin.unrealized_conversion_cast %26 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                
    %28 = ptr_xdsl.from_ptr %27 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                               
    %29 = ptr_xdsl.to_ptr %25 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    %30 = ptr_xdsl.load %29 : !ptr_xdsl.ptr -> i64                                                                                                                                           
    %31 = ptr_xdsl.to_ptr %28 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    ptr_xdsl.store %30, %31 : i64, !ptr_xdsl.ptr                                                                                                                                             
    %32 = ptr_xdsl.to_ptr %28 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    %33 = ptr_xdsl.load %32 : !ptr_xdsl.ptr -> i64                                                                                                                                           
    %34 = llvm.inttoptr %33 : i64 to !llvm.ptr                                                                                                                                               
    %35 = builtin.unrealized_conversion_cast %34 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                
    %36 = ptr_xdsl.from_ptr %35 : !ptr_xdsl.ptr -> memref<120xi8>                                                                                                                            
    %37 = ptr_xdsl.to_ptr %36 : memref<120xi8> -> !ptr_xdsl.ptr                                                                                                                              
    %bytes_per_element = arith.constant 1 : index                                                                                                                                            
    %scaled_pointer_offset = arith.muli %const3.index, %bytes_per_element : index                                                                                                            
    %offset_pointer = ptr_xdsl.ptradd %37, %scaled_pointer_offset : (!ptr_xdsl.ptr, index) -> !ptr_xdsl.ptr                                                                                  
    %38 = ptr_xdsl.from_ptr %offset_pointer : !ptr_xdsl.ptr -> memref<24xi8>                                                                                                                 
    %39 = memref.view %38[%const8.index][] : memref<24xi8> to memref<i64>                                                                                                                    
    %c1_4 = arith.constant 1 : i32                                                                                                                                                           
    %40 = llvm.alloca %c1_4 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
    %41 = builtin.unrealized_conversion_cast %40 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                
    %42 = ptr_xdsl.from_ptr %41 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                               
    %43 = ptr_xdsl.to_ptr %39 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    %44 = ptr_xdsl.load %43 : !ptr_xdsl.ptr -> i64                                                                                                                                           
    %45 = ptr_xdsl.to_ptr %42 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    ptr_xdsl.store %44, %45 : i64, !ptr_xdsl.ptr                                                                                                                                             
    %46 = ptr_xdsl.to_ptr %42 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                 
    %47 = ptr_xdsl.load %46 : !ptr_xdsl.ptr -> i64                                                                                                                                           
    func.return %47 : i64                                                                                                                                                                    
  }                                                                                                                                                                                          
}                                                                                                                                                                                            


────── xDSL afte ConvertPtrToLLVMPass passe
--- before                                                                                                                                                                                   
+++ xDSL afte ConvertPtrToLLVMPass passe                                                                                                                                                     
@@ -5,65 +5,68 @@                                                                                                                                                                            
     %const3.index = arith.constant 3 : index                                                                                                                                                
     %c1 = arith.constant 1 : i32                                                                                                                                                            
     %0 = llvm.alloca %c1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                  
-    %1 = builtin.unrealized_conversion_cast %0 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                 
-    %2 = ptr_xdsl.from_ptr %1 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                                
-    %3 = ptr_xdsl.to_ptr %2 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                  
-    ptr_xdsl.store %simuReferenceArg, %3 : i64, !ptr_xdsl.ptr                                                                                                                               
+    %1 = builtin.unrealized_conversion_cast %0 : !llvm.ptr to !llvm.ptr                                                                                                                     
+    %2 = builtin.unrealized_conversion_cast %1 : !llvm.ptr to !llvm.ptr                                                                                                                     
+    llvm.store %simuReferenceArg, %2 : i64, !llvm.ptr                                                                                                                                       
     %c1_1 = arith.constant 1 : i32                                                                                                                                                          
-    %4 = llvm.alloca %c1_1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
-    %5 = builtin.unrealized_conversion_cast %4 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                                 
-    %6 = ptr_xdsl.from_ptr %5 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                                
-    %7 = ptr_xdsl.to_ptr %6 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                  
-    ptr_xdsl.store %iArg, %7 : i64, !ptr_xdsl.ptr                                                                                                                                           
-    %8 = ptr_xdsl.to_ptr %2 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                  
-    %9 = ptr_xdsl.load %8 : !ptr_xdsl.ptr -> i64                                                                                                                                            
-    %10 = llvm.inttoptr %9 : i64 to !llvm.ptr                                                                                                                                               
-    %11 = builtin.unrealized_conversion_cast %10 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %12 = ptr_xdsl.from_ptr %11 : !ptr_xdsl.ptr -> memref<32xi8>                                                                                                                            
-    %13 = memref.view %12[%const0.index][] : memref<32xi8> to memref<i64>                                                                                                                   
+    %3 = llvm.alloca %c1_1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
+    %4 = builtin.unrealized_conversion_cast %3 : !llvm.ptr to !llvm.ptr                                                                                                                     
+    %5 = builtin.unrealized_conversion_cast %4 : !llvm.ptr to !llvm.ptr                                                                                                                     
+    llvm.store %iArg, %5 : i64, !llvm.ptr                                                                                                                                                   
+    %6 = builtin.unrealized_conversion_cast %1 : !llvm.ptr to !llvm.ptr                                                                                                                     
+    %7 = llvm.load %6 : !llvm.ptr -> i64                                                                                                                                                    
+    %8 = llvm.inttoptr %7 : i64 to !llvm.ptr                                                                                                                                                
+    %9 = builtin.unrealized_conversion_cast %8 : !llvm.ptr to !llvm.ptr                                                                                                                     
+    %10 = memref.view %9[%const0.index][] : !llvm.ptr to memref<i64>                                                                                                                        
     %c1_2 = arith.constant 1 : i32                                                                                                                                                          
-    %14 = llvm.alloca %c1_2 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
-    %15 = builtin.unrealized_conversion_cast %14 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %16 = ptr_xdsl.from_ptr %15 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                              
-    %17 = ptr_xdsl.to_ptr %13 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    %18 = ptr_xdsl.load %17 : !ptr_xdsl.ptr -> i64                                                                                                                                          
-    %19 = ptr_xdsl.to_ptr %16 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    ptr_xdsl.store %18, %19 : i64, !ptr_xdsl.ptr                                                                                                                                            
-    %20 = ptr_xdsl.to_ptr %16 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    %21 = ptr_xdsl.load %20 : !ptr_xdsl.ptr -> i64                                                                                                                                          
-    %22 = llvm.inttoptr %21 : i64 to !llvm.ptr                                                                                                                                              
-    %23 = builtin.unrealized_conversion_cast %22 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %24 = ptr_xdsl.from_ptr %23 : !ptr_xdsl.ptr -> memref<16xi8>                                                                                                                            
-    %25 = memref.view %24[%const0.index][] : memref<16xi8> to memref<i64>                                                                                                                   
+    %11 = llvm.alloca %c1_2 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
+    %12 = builtin.unrealized_conversion_cast %11 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %13 = "memref.extract_aligned_pointer_as_index"(%10) : (memref<i64>) -> index                                                                                                           
+    %14 = arith.index_cast %13 : index to i64                                                                                                                                               
+    %15 = llvm.inttoptr %14 : i64 to !llvm.ptr                                                                                                                                              
+    %16 = builtin.unrealized_conversion_cast %15 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %17 = llvm.load %16 : !llvm.ptr -> i64                                                                                                                                                  
+    %18 = builtin.unrealized_conversion_cast %12 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    llvm.store %17, %18 : i64, !llvm.ptr                                                                                                                                                    
+    %19 = builtin.unrealized_conversion_cast %12 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %20 = llvm.load %19 : !llvm.ptr -> i64                                                                                                                                                  
+    %21 = llvm.inttoptr %20 : i64 to !llvm.ptr                                                                                                                                              
+    %22 = builtin.unrealized_conversion_cast %21 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %23 = memref.view %22[%const0.index][] : !llvm.ptr to memref<i64>                                                                                                                       
     %c1_3 = arith.constant 1 : i32                                                                                                                                                          
-    %26 = llvm.alloca %c1_3 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
-    %27 = builtin.unrealized_conversion_cast %26 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %28 = ptr_xdsl.from_ptr %27 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                              
-    %29 = ptr_xdsl.to_ptr %25 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    %30 = ptr_xdsl.load %29 : !ptr_xdsl.ptr -> i64                                                                                                                                          
-    %31 = ptr_xdsl.to_ptr %28 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    ptr_xdsl.store %30, %31 : i64, !ptr_xdsl.ptr                                                                                                                                            
-    %32 = ptr_xdsl.to_ptr %28 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    %33 = ptr_xdsl.load %32 : !ptr_xdsl.ptr -> i64                                                                                                                                          
+    %24 = llvm.alloca %c1_3 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
+    %25 = builtin.unrealized_conversion_cast %24 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %26 = "memref.extract_aligned_pointer_as_index"(%23) : (memref<i64>) -> index                                                                                                           
+    %27 = arith.index_cast %26 : index to i64                                                                                                                                               
+    %28 = llvm.inttoptr %27 : i64 to !llvm.ptr                                                                                                                                              
+    %29 = builtin.unrealized_conversion_cast %28 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %30 = llvm.load %29 : !llvm.ptr -> i64                                                                                                                                                  
+    %31 = builtin.unrealized_conversion_cast %25 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    llvm.store %30, %31 : i64, !llvm.ptr                                                                                                                                                    
+    %32 = builtin.unrealized_conversion_cast %25 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %33 = llvm.load %32 : !llvm.ptr -> i64                                                                                                                                                  
     %34 = llvm.inttoptr %33 : i64 to !llvm.ptr                                                                                                                                              
-    %35 = builtin.unrealized_conversion_cast %34 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %36 = ptr_xdsl.from_ptr %35 : !ptr_xdsl.ptr -> memref<120xi8>                                                                                                                           
-    %37 = ptr_xdsl.to_ptr %36 : memref<120xi8> -> !ptr_xdsl.ptr                                                                                                                             
+    %35 = builtin.unrealized_conversion_cast %34 : !llvm.ptr to !llvm.ptr                                                                                                                   
     %bytes_per_element = arith.constant 1 : index                                                                                                                                           
     %scaled_pointer_offset = arith.muli %const3.index, %bytes_per_element : index                                                                                                           
-    %offset_pointer = ptr_xdsl.ptradd %37, %scaled_pointer_offset : (!ptr_xdsl.ptr, index) -> !ptr_xdsl.ptr                                                                                 
-    %38 = ptr_xdsl.from_ptr %offset_pointer : !ptr_xdsl.ptr -> memref<24xi8>                                                                                                                
-    %39 = memref.view %38[%const8.index][] : memref<24xi8> to memref<i64>                                                                                                                   
+    %offset_pointer = builtin.unrealized_conversion_cast %35 : !llvm.ptr to !llvm.ptr                                                                                                       
+    %offset_pointer_1 = arith.index_cast %scaled_pointer_offset : index to i64                                                                                                              
+    %offset_pointer_2 = llvm.ptrtoint %offset_pointer : !llvm.ptr to i64                                                                                                                    
+    %offset_pointer_3 = arith.addi %offset_pointer_2, %offset_pointer_1 : i64                                                                                                               
+    %offset_pointer_4 = llvm.inttoptr %offset_pointer_3 : i64 to !llvm.ptr                                                                                                                  
+    %36 = memref.view %offset_pointer_4[%const8.index][] : !llvm.ptr to memref<i64>                                                                                                         
     %c1_4 = arith.constant 1 : i32                                                                                                                                                          
-    %40 = llvm.alloca %c1_4 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
-    %41 = builtin.unrealized_conversion_cast %40 : !llvm.ptr to !ptr_xdsl.ptr                                                                                                               
-    %42 = ptr_xdsl.from_ptr %41 : !ptr_xdsl.ptr -> memref<i64>                                                                                                                              
-    %43 = ptr_xdsl.to_ptr %39 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    %44 = ptr_xdsl.load %43 : !ptr_xdsl.ptr -> i64                                                                                                                                          
-    %45 = ptr_xdsl.to_ptr %42 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    ptr_xdsl.store %44, %45 : i64, !ptr_xdsl.ptr                                                                                                                                            
-    %46 = ptr_xdsl.to_ptr %42 : memref<i64> -> !ptr_xdsl.ptr                                                                                                                                
-    %47 = ptr_xdsl.load %46 : !ptr_xdsl.ptr -> i64                                                                                                                                          
-    func.return %47 : i64                                                                                                                                                                   
+    %37 = llvm.alloca %c1_4 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                               
+    %38 = builtin.unrealized_conversion_cast %37 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %39 = "memref.extract_aligned_pointer_as_index"(%36) : (memref<i64>) -> index                                                                                                           
+    %40 = arith.index_cast %39 : index to i64                                                                                                                                               
+    %41 = llvm.inttoptr %40 : i64 to !llvm.ptr                                                                                                                                              
+    %42 = builtin.unrealized_conversion_cast %41 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %43 = llvm.load %42 : !llvm.ptr -> i64                                                                                                                                                  
+    %44 = builtin.unrealized_conversion_cast %38 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    llvm.store %43, %44 : i64, !llvm.ptr                                                                                                                                                    
+    %45 = builtin.unrealized_conversion_cast %38 : !llvm.ptr to !llvm.ptr                                                                                                                   
+    %46 = llvm.load %45 : !llvm.ptr -> i64                                                                                                                                                  
+    func.return %46 : i64                                                                                                                                                                   
   }                                                                                                                                                                                         
 }                                                                                                                                                                                           


────── MLIR
builtin.module {                                                                                                                                                                             
  func.func @xdsl_main(%simuReferenceArg: i64, %iArg: i64) -> i64 attributes {llvm.emit_c_interface} {                                                                                       
    %const8.index = arith.constant 8 : index                                                                                                                                                 
    %const0.index = arith.constant 0 : index                                                                                                                                                 
    %const3.index = arith.constant 3 : index                                                                                                                                                 
    %c1 = arith.constant 1 : i32                                                                                                                                                             
    %0 = llvm.alloca %c1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                   
    %1 = builtin.unrealized_conversion_cast %0 : !llvm.ptr to !llvm.ptr                                                                                                                      
    %2 = builtin.unrealized_conversion_cast %1 : !llvm.ptr to !llvm.ptr                                                                                                                      
    llvm.store %simuReferenceArg, %2 : i64, !llvm.ptr                                                                                                                                        
    %c1_1 = arith.constant 1 : i32                                                                                                                                                           
    %3 = llvm.alloca %c1_1 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                 
    %4 = builtin.unrealized_conversion_cast %3 : !llvm.ptr to !llvm.ptr                                                                                                                      
    %5 = builtin.unrealized_conversion_cast %4 : !llvm.ptr to !llvm.ptr                                                                                                                      
    llvm.store %iArg, %5 : i64, !llvm.ptr                                                                                                                                                    
    %6 = builtin.unrealized_conversion_cast %1 : !llvm.ptr to !llvm.ptr                                                                                                                      
    %7 = llvm.load %6 : !llvm.ptr -> i64                                                                                                                                                     
    %8 = llvm.inttoptr %7 : i64 to !llvm.ptr                                                                                                                                                 
    %9 = builtin.unrealized_conversion_cast %8 : !llvm.ptr to !llvm.ptr                                                                                                                      
    %10 = memref.view %9[%const0.index][] : !llvm.ptr to memref<i64>                                                                                                                         
    %c1_2 = arith.constant 1 : i32                                                                                                                                                           
    %11 = llvm.alloca %c1_2 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
    %12 = builtin.unrealized_conversion_cast %11 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %13 = "memref.extract_aligned_pointer_as_index"(%10) : (memref<i64>) -> index                                                                                                            
    %14 = arith.index_cast %13 : index to i64                                                                                                                                                
    %15 = llvm.inttoptr %14 : i64 to !llvm.ptr                                                                                                                                               
    %16 = builtin.unrealized_conversion_cast %15 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %17 = llvm.load %16 : !llvm.ptr -> i64                                                                                                                                                   
    %18 = builtin.unrealized_conversion_cast %12 : !llvm.ptr to !llvm.ptr                                                                                                                    
    llvm.store %17, %18 : i64, !llvm.ptr                                                                                                                                                     
    %19 = builtin.unrealized_conversion_cast %12 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %20 = llvm.load %19 : !llvm.ptr -> i64                                                                                                                                                   
    %21 = llvm.inttoptr %20 : i64 to !llvm.ptr                                                                                                                                               
    %22 = builtin.unrealized_conversion_cast %21 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %23 = memref.view %22[%const0.index][] : !llvm.ptr to memref<i64>                                                                                                                        
    %c1_3 = arith.constant 1 : i32                                                                                                                                                           
    %24 = llvm.alloca %c1_3 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
    %25 = builtin.unrealized_conversion_cast %24 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %26 = "memref.extract_aligned_pointer_as_index"(%23) : (memref<i64>) -> index                                                                                                            
    %27 = arith.index_cast %26 : index to i64                                                                                                                                                
    %28 = llvm.inttoptr %27 : i64 to !llvm.ptr                                                                                                                                               
    %29 = builtin.unrealized_conversion_cast %28 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %30 = llvm.load %29 : !llvm.ptr -> i64                                                                                                                                                   
    %31 = builtin.unrealized_conversion_cast %25 : !llvm.ptr to !llvm.ptr                                                                                                                    
    llvm.store %30, %31 : i64, !llvm.ptr                                                                                                                                                     
    %32 = builtin.unrealized_conversion_cast %25 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %33 = llvm.load %32 : !llvm.ptr -> i64                                                                                                                                                   
    %34 = llvm.inttoptr %33 : i64 to !llvm.ptr                                                                                                                                               
    %35 = builtin.unrealized_conversion_cast %34 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %bytes_per_element = arith.constant 1 : index                                                                                                                                            
    %scaled_pointer_offset = arith.muli %const3.index, %bytes_per_element : index                                                                                                            
    %offset_pointer = builtin.unrealized_conversion_cast %35 : !llvm.ptr to !llvm.ptr                                                                                                        
    %offset_pointer_1 = arith.index_cast %scaled_pointer_offset : index to i64                                                                                                               
    %offset_pointer_2 = llvm.ptrtoint %offset_pointer : !llvm.ptr to i64                                                                                                                     
    %offset_pointer_3 = arith.addi %offset_pointer_2, %offset_pointer_1 : i64                                                                                                                
    %offset_pointer_4 = llvm.inttoptr %offset_pointer_3 : i64 to !llvm.ptr                                                                                                                   
    %36 = memref.view %offset_pointer_4[%const8.index][] : !llvm.ptr to memref<i64>                                                                                                          
    %c1_4 = arith.constant 1 : i32                                                                                                                                                           
    %37 = llvm.alloca %c1_4 x i64 {alignment = 32 : i64} : (i32) -> !llvm.ptr                                                                                                                
    %38 = builtin.unrealized_conversion_cast %37 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %39 = "memref.extract_aligned_pointer_as_index"(%36) : (memref<i64>) -> index                                                                                                            
    %40 = arith.index_cast %39 : index to i64                                                                                                                                                
    %41 = llvm.inttoptr %40 : i64 to !llvm.ptr                                                                                                                                               
    %42 = builtin.unrealized_conversion_cast %41 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %43 = llvm.load %42 : !llvm.ptr -> i64                                                                                                                                                   
    %44 = builtin.unrealized_conversion_cast %38 : !llvm.ptr to !llvm.ptr                                                                                                                    
    llvm.store %43, %44 : i64, !llvm.ptr                                                                                                                                                     
    %45 = builtin.unrealized_conversion_cast %38 : !llvm.ptr to !llvm.ptr                                                                                                                    
    %46 = llvm.load %45 : !llvm.ptr -> i64                                                                                                                                                   
    func.return %46 : i64                                                                                                                                                                    
  }                                                                                                                                                                                          
}                                                                                                                                                                                            


Error when running mlir-opt :
Full command: /home/lmx/code/llvm-project/build-mlir/bin/mlir-opt
        --convert-index-to-llvm
        --loop-invariant-code-motion
        --cse
        --canonicalize
        --symbol-dce
        --mem2reg
        --expand-strided-metadata
        --normalize-memrefs
        --memref-expand
        --fold-memref-alias-ops
        --mlir-print-ir-after-all /home/lmx/git/xdsl-json/build/ptr_struct_nested.mlir
        -o /home/lmx/git/xdsl-json/build/ptr_struct_nested.mlir.opt

/home/lmx/git/xdsl-json/build/ptr_struct_nested.mlir:20:45: error: custom op 'memref.view' invalid kind of type specified: expected builtin.memref, but found '!llvm.ptr'
    %10 = memref.view %9[%const0.index][] : !llvm.ptr to memref<i64>
```