"""OCCT package Quantity (toolkit TKernel)"""

import enum
from typing import overload

import nanoocp.BVH
import nanoocp.Standard
import nanoocp.TCollection


class Quantity_NameOfColor(enum.IntEnum):
    """
    Definition of names of known colors.
    The names come (mostly) from the X11 specification.
    """

    Quantity_NOC_BLACK = 0

    Quantity_NOC_MATRABLUE = 1

    Quantity_NOC_MATRAGRAY = 2

    Quantity_NOC_ALICEBLUE = 3

    Quantity_NOC_ANTIQUEWHITE = 4

    Quantity_NOC_ANTIQUEWHITE1 = 5

    Quantity_NOC_ANTIQUEWHITE2 = 6

    Quantity_NOC_ANTIQUEWHITE3 = 7

    Quantity_NOC_ANTIQUEWHITE4 = 8

    Quantity_NOC_AQUAMARINE1 = 9

    Quantity_NOC_AQUAMARINE2 = 10

    Quantity_NOC_AQUAMARINE4 = 11

    Quantity_NOC_AZURE = 12

    Quantity_NOC_AZURE2 = 13

    Quantity_NOC_AZURE3 = 14

    Quantity_NOC_AZURE4 = 15

    Quantity_NOC_BEIGE = 16

    Quantity_NOC_BISQUE = 17

    Quantity_NOC_BISQUE2 = 18

    Quantity_NOC_BISQUE3 = 19

    Quantity_NOC_BISQUE4 = 20

    Quantity_NOC_BLANCHEDALMOND = 21

    Quantity_NOC_BLUE = 22

    Quantity_NOC_BLUE1 = 22

    Quantity_NOC_BLUE2 = 23

    Quantity_NOC_BLUE3 = 24

    Quantity_NOC_BLUE4 = 25

    Quantity_NOC_BLUEVIOLET = 26

    Quantity_NOC_BROWN = 27

    Quantity_NOC_BROWN1 = 28

    Quantity_NOC_BROWN2 = 29

    Quantity_NOC_BROWN3 = 30

    Quantity_NOC_BROWN4 = 31

    Quantity_NOC_BURLYWOOD = 32

    Quantity_NOC_BURLYWOOD1 = 33

    Quantity_NOC_BURLYWOOD2 = 34

    Quantity_NOC_BURLYWOOD3 = 35

    Quantity_NOC_BURLYWOOD4 = 36

    Quantity_NOC_CADETBLUE = 37

    Quantity_NOC_CADETBLUE1 = 38

    Quantity_NOC_CADETBLUE2 = 39

    Quantity_NOC_CADETBLUE3 = 40

    Quantity_NOC_CADETBLUE4 = 41

    Quantity_NOC_CHARTREUSE = 42

    Quantity_NOC_CHARTREUSE1 = 42

    Quantity_NOC_CHARTREUSE2 = 43

    Quantity_NOC_CHARTREUSE3 = 44

    Quantity_NOC_CHARTREUSE4 = 45

    Quantity_NOC_CHOCOLATE = 46

    Quantity_NOC_CHOCOLATE1 = 47

    Quantity_NOC_CHOCOLATE2 = 48

    Quantity_NOC_CHOCOLATE3 = 49

    Quantity_NOC_CHOCOLATE4 = 50

    Quantity_NOC_CORAL = 51

    Quantity_NOC_CORAL1 = 52

    Quantity_NOC_CORAL2 = 53

    Quantity_NOC_CORAL3 = 54

    Quantity_NOC_CORAL4 = 55

    Quantity_NOC_CORNFLOWERBLUE = 56

    Quantity_NOC_CORNSILK1 = 57

    Quantity_NOC_CORNSILK2 = 58

    Quantity_NOC_CORNSILK3 = 59

    Quantity_NOC_CORNSILK4 = 60

    Quantity_NOC_CYAN = 61

    Quantity_NOC_CYAN1 = 61

    Quantity_NOC_CYAN2 = 62

    Quantity_NOC_CYAN3 = 63

    Quantity_NOC_CYAN4 = 64

    Quantity_NOC_DARKGOLDENROD = 65

    Quantity_NOC_DARKGOLDENROD1 = 66

    Quantity_NOC_DARKGOLDENROD2 = 67

    Quantity_NOC_DARKGOLDENROD3 = 68

    Quantity_NOC_DARKGOLDENROD4 = 69

    Quantity_NOC_DARKGREEN = 70

    Quantity_NOC_DARKKHAKI = 71

    Quantity_NOC_DARKOLIVEGREEN = 72

    Quantity_NOC_DARKOLIVEGREEN1 = 73

    Quantity_NOC_DARKOLIVEGREEN2 = 74

    Quantity_NOC_DARKOLIVEGREEN3 = 75

    Quantity_NOC_DARKOLIVEGREEN4 = 76

    Quantity_NOC_DARKORANGE = 77

    Quantity_NOC_DARKORANGE1 = 78

    Quantity_NOC_DARKORANGE2 = 79

    Quantity_NOC_DARKORANGE3 = 80

    Quantity_NOC_DARKORANGE4 = 81

    Quantity_NOC_DARKORCHID = 82

    Quantity_NOC_DARKORCHID1 = 83

    Quantity_NOC_DARKORCHID2 = 84

    Quantity_NOC_DARKORCHID3 = 85

    Quantity_NOC_DARKORCHID4 = 86

    Quantity_NOC_DARKSALMON = 87

    Quantity_NOC_DARKSEAGREEN = 88

    Quantity_NOC_DARKSEAGREEN1 = 89

    Quantity_NOC_DARKSEAGREEN2 = 90

    Quantity_NOC_DARKSEAGREEN3 = 91

    Quantity_NOC_DARKSEAGREEN4 = 92

    Quantity_NOC_DARKSLATEBLUE = 93

    Quantity_NOC_DARKSLATEGRAY1 = 94

    Quantity_NOC_DARKSLATEGRAY2 = 95

    Quantity_NOC_DARKSLATEGRAY3 = 96

    Quantity_NOC_DARKSLATEGRAY4 = 97

    Quantity_NOC_DARKSLATEGRAY = 98

    Quantity_NOC_DARKTURQUOISE = 99

    Quantity_NOC_DARKVIOLET = 100

    Quantity_NOC_DEEPPINK = 101

    Quantity_NOC_DEEPPINK2 = 102

    Quantity_NOC_DEEPPINK3 = 103

    Quantity_NOC_DEEPPINK4 = 104

    Quantity_NOC_DEEPSKYBLUE1 = 105

    Quantity_NOC_DEEPSKYBLUE2 = 106

    Quantity_NOC_DEEPSKYBLUE3 = 107

    Quantity_NOC_DEEPSKYBLUE4 = 108

    Quantity_NOC_DODGERBLUE1 = 109

    Quantity_NOC_DODGERBLUE2 = 110

    Quantity_NOC_DODGERBLUE3 = 111

    Quantity_NOC_DODGERBLUE4 = 112

    Quantity_NOC_FIREBRICK = 113

    Quantity_NOC_FIREBRICK1 = 114

    Quantity_NOC_FIREBRICK2 = 115

    Quantity_NOC_FIREBRICK3 = 116

    Quantity_NOC_FIREBRICK4 = 117

    Quantity_NOC_FLORALWHITE = 118

    Quantity_NOC_FORESTGREEN = 119

    Quantity_NOC_GAINSBORO = 120

    Quantity_NOC_GHOSTWHITE = 121

    Quantity_NOC_GOLD = 122

    Quantity_NOC_GOLD1 = 122

    Quantity_NOC_GOLD2 = 123

    Quantity_NOC_GOLD3 = 124

    Quantity_NOC_GOLD4 = 125

    Quantity_NOC_GOLDENROD = 126

    Quantity_NOC_GOLDENROD1 = 127

    Quantity_NOC_GOLDENROD2 = 128

    Quantity_NOC_GOLDENROD3 = 129

    Quantity_NOC_GOLDENROD4 = 130

    Quantity_NOC_GRAY = 131

    Quantity_NOC_GRAY0 = 132

    Quantity_NOC_GRAY1 = 133

    Quantity_NOC_GRAY2 = 134

    Quantity_NOC_GRAY3 = 135

    Quantity_NOC_GRAY4 = 136

    Quantity_NOC_GRAY5 = 137

    Quantity_NOC_GRAY6 = 138

    Quantity_NOC_GRAY7 = 139

    Quantity_NOC_GRAY8 = 140

    Quantity_NOC_GRAY9 = 141

    Quantity_NOC_GRAY10 = 142

    Quantity_NOC_GRAY11 = 143

    Quantity_NOC_GRAY12 = 144

    Quantity_NOC_GRAY13 = 145

    Quantity_NOC_GRAY14 = 146

    Quantity_NOC_GRAY15 = 147

    Quantity_NOC_GRAY16 = 148

    Quantity_NOC_GRAY17 = 149

    Quantity_NOC_GRAY18 = 150

    Quantity_NOC_GRAY19 = 151

    Quantity_NOC_GRAY20 = 152

    Quantity_NOC_GRAY21 = 153

    Quantity_NOC_GRAY22 = 154

    Quantity_NOC_GRAY23 = 155

    Quantity_NOC_GRAY24 = 156

    Quantity_NOC_GRAY25 = 157

    Quantity_NOC_GRAY26 = 158

    Quantity_NOC_GRAY27 = 159

    Quantity_NOC_GRAY28 = 160

    Quantity_NOC_GRAY29 = 161

    Quantity_NOC_GRAY30 = 162

    Quantity_NOC_GRAY31 = 163

    Quantity_NOC_GRAY32 = 164

    Quantity_NOC_GRAY33 = 165

    Quantity_NOC_GRAY34 = 166

    Quantity_NOC_GRAY35 = 167

    Quantity_NOC_GRAY36 = 168

    Quantity_NOC_GRAY37 = 169

    Quantity_NOC_GRAY38 = 170

    Quantity_NOC_GRAY39 = 171

    Quantity_NOC_GRAY40 = 172

    Quantity_NOC_GRAY41 = 173

    Quantity_NOC_GRAY42 = 174

    Quantity_NOC_GRAY43 = 175

    Quantity_NOC_GRAY44 = 176

    Quantity_NOC_GRAY45 = 177

    Quantity_NOC_GRAY46 = 178

    Quantity_NOC_GRAY47 = 179

    Quantity_NOC_GRAY48 = 180

    Quantity_NOC_GRAY49 = 181

    Quantity_NOC_GRAY50 = 182

    Quantity_NOC_GRAY51 = 183

    Quantity_NOC_GRAY52 = 184

    Quantity_NOC_GRAY53 = 185

    Quantity_NOC_GRAY54 = 186

    Quantity_NOC_GRAY55 = 187

    Quantity_NOC_GRAY56 = 188

    Quantity_NOC_GRAY57 = 189

    Quantity_NOC_GRAY58 = 190

    Quantity_NOC_GRAY59 = 191

    Quantity_NOC_GRAY60 = 192

    Quantity_NOC_GRAY61 = 193

    Quantity_NOC_GRAY62 = 194

    Quantity_NOC_GRAY63 = 195

    Quantity_NOC_GRAY64 = 196

    Quantity_NOC_GRAY65 = 197

    Quantity_NOC_GRAY66 = 198

    Quantity_NOC_GRAY67 = 199

    Quantity_NOC_GRAY68 = 200

    Quantity_NOC_GRAY69 = 201

    Quantity_NOC_GRAY70 = 202

    Quantity_NOC_GRAY71 = 203

    Quantity_NOC_GRAY72 = 204

    Quantity_NOC_GRAY73 = 205

    Quantity_NOC_GRAY74 = 206

    Quantity_NOC_GRAY75 = 207

    Quantity_NOC_GRAY76 = 208

    Quantity_NOC_GRAY77 = 209

    Quantity_NOC_GRAY78 = 210

    Quantity_NOC_GRAY79 = 211

    Quantity_NOC_GRAY80 = 212

    Quantity_NOC_GRAY81 = 213

    Quantity_NOC_GRAY82 = 214

    Quantity_NOC_GRAY83 = 215

    Quantity_NOC_GRAY85 = 216

    Quantity_NOC_GRAY86 = 217

    Quantity_NOC_GRAY87 = 218

    Quantity_NOC_GRAY88 = 219

    Quantity_NOC_GRAY89 = 220

    Quantity_NOC_GRAY90 = 221

    Quantity_NOC_GRAY91 = 222

    Quantity_NOC_GRAY92 = 223

    Quantity_NOC_GRAY93 = 224

    Quantity_NOC_GRAY94 = 225

    Quantity_NOC_GRAY95 = 226

    Quantity_NOC_GRAY97 = 227

    Quantity_NOC_GRAY98 = 228

    Quantity_NOC_GRAY99 = 229

    Quantity_NOC_GREEN = 230

    Quantity_NOC_GREEN1 = 230

    Quantity_NOC_GREEN2 = 231

    Quantity_NOC_GREEN3 = 232

    Quantity_NOC_GREEN4 = 233

    Quantity_NOC_GREENYELLOW = 234

    Quantity_NOC_HONEYDEW = 235

    Quantity_NOC_HONEYDEW2 = 236

    Quantity_NOC_HONEYDEW3 = 237

    Quantity_NOC_HONEYDEW4 = 238

    Quantity_NOC_HOTPINK = 239

    Quantity_NOC_HOTPINK1 = 240

    Quantity_NOC_HOTPINK2 = 241

    Quantity_NOC_HOTPINK3 = 242

    Quantity_NOC_HOTPINK4 = 243

    Quantity_NOC_INDIANRED = 244

    Quantity_NOC_INDIANRED1 = 245

    Quantity_NOC_INDIANRED2 = 246

    Quantity_NOC_INDIANRED3 = 247

    Quantity_NOC_INDIANRED4 = 248

    Quantity_NOC_IVORY = 249

    Quantity_NOC_IVORY2 = 250

    Quantity_NOC_IVORY3 = 251

    Quantity_NOC_IVORY4 = 252

    Quantity_NOC_KHAKI = 253

    Quantity_NOC_KHAKI1 = 254

    Quantity_NOC_KHAKI2 = 255

    Quantity_NOC_KHAKI3 = 256

    Quantity_NOC_KHAKI4 = 257

    Quantity_NOC_LAVENDER = 258

    Quantity_NOC_LAVENDERBLUSH1 = 259

    Quantity_NOC_LAVENDERBLUSH2 = 260

    Quantity_NOC_LAVENDERBLUSH3 = 261

    Quantity_NOC_LAVENDERBLUSH4 = 262

    Quantity_NOC_LAWNGREEN = 263

    Quantity_NOC_LEMONCHIFFON1 = 264

    Quantity_NOC_LEMONCHIFFON2 = 265

    Quantity_NOC_LEMONCHIFFON3 = 266

    Quantity_NOC_LEMONCHIFFON4 = 267

    Quantity_NOC_LIGHTBLUE = 268

    Quantity_NOC_LIGHTBLUE1 = 269

    Quantity_NOC_LIGHTBLUE2 = 270

    Quantity_NOC_LIGHTBLUE3 = 271

    Quantity_NOC_LIGHTBLUE4 = 272

    Quantity_NOC_LIGHTCORAL = 273

    Quantity_NOC_LIGHTCYAN = 274

    Quantity_NOC_LIGHTCYAN1 = 274

    Quantity_NOC_LIGHTCYAN2 = 275

    Quantity_NOC_LIGHTCYAN3 = 276

    Quantity_NOC_LIGHTCYAN4 = 277

    Quantity_NOC_LIGHTGOLDENROD = 278

    Quantity_NOC_LIGHTGOLDENROD1 = 279

    Quantity_NOC_LIGHTGOLDENROD2 = 280

    Quantity_NOC_LIGHTGOLDENROD3 = 281

    Quantity_NOC_LIGHTGOLDENROD4 = 282

    Quantity_NOC_LIGHTGOLDENRODYELLOW = 283

    Quantity_NOC_LIGHTGRAY = 284

    Quantity_NOC_LIGHTPINK = 285

    Quantity_NOC_LIGHTPINK1 = 286

    Quantity_NOC_LIGHTPINK2 = 287

    Quantity_NOC_LIGHTPINK3 = 288

    Quantity_NOC_LIGHTPINK4 = 289

    Quantity_NOC_LIGHTSALMON1 = 290

    Quantity_NOC_LIGHTSALMON2 = 291

    Quantity_NOC_LIGHTSALMON3 = 292

    Quantity_NOC_LIGHTSALMON4 = 293

    Quantity_NOC_LIGHTSEAGREEN = 294

    Quantity_NOC_LIGHTSKYBLUE = 295

    Quantity_NOC_LIGHTSKYBLUE1 = 296

    Quantity_NOC_LIGHTSKYBLUE2 = 297

    Quantity_NOC_LIGHTSKYBLUE3 = 298

    Quantity_NOC_LIGHTSKYBLUE4 = 299

    Quantity_NOC_LIGHTSLATEBLUE = 300

    Quantity_NOC_LIGHTSLATEGRAY = 301

    Quantity_NOC_LIGHTSTEELBLUE = 302

    Quantity_NOC_LIGHTSTEELBLUE1 = 303

    Quantity_NOC_LIGHTSTEELBLUE2 = 304

    Quantity_NOC_LIGHTSTEELBLUE3 = 305

    Quantity_NOC_LIGHTSTEELBLUE4 = 306

    Quantity_NOC_LIGHTYELLOW = 307

    Quantity_NOC_LIGHTYELLOW2 = 308

    Quantity_NOC_LIGHTYELLOW3 = 309

    Quantity_NOC_LIGHTYELLOW4 = 310

    Quantity_NOC_LIMEGREEN = 311

    Quantity_NOC_LINEN = 312

    Quantity_NOC_MAGENTA = 313

    Quantity_NOC_MAGENTA1 = 313

    Quantity_NOC_MAGENTA2 = 314

    Quantity_NOC_MAGENTA3 = 315

    Quantity_NOC_MAGENTA4 = 316

    Quantity_NOC_MAROON = 317

    Quantity_NOC_MAROON1 = 318

    Quantity_NOC_MAROON2 = 319

    Quantity_NOC_MAROON3 = 320

    Quantity_NOC_MAROON4 = 321

    Quantity_NOC_MEDIUMAQUAMARINE = 322

    Quantity_NOC_MEDIUMORCHID = 323

    Quantity_NOC_MEDIUMORCHID1 = 324

    Quantity_NOC_MEDIUMORCHID2 = 325

    Quantity_NOC_MEDIUMORCHID3 = 326

    Quantity_NOC_MEDIUMORCHID4 = 327

    Quantity_NOC_MEDIUMPURPLE = 328

    Quantity_NOC_MEDIUMPURPLE1 = 329

    Quantity_NOC_MEDIUMPURPLE2 = 330

    Quantity_NOC_MEDIUMPURPLE3 = 331

    Quantity_NOC_MEDIUMPURPLE4 = 332

    Quantity_NOC_MEDIUMSEAGREEN = 333

    Quantity_NOC_MEDIUMSLATEBLUE = 334

    Quantity_NOC_MEDIUMSPRINGGREEN = 335

    Quantity_NOC_MEDIUMTURQUOISE = 336

    Quantity_NOC_MEDIUMVIOLETRED = 337

    Quantity_NOC_MIDNIGHTBLUE = 338

    Quantity_NOC_MINTCREAM = 339

    Quantity_NOC_MISTYROSE = 340

    Quantity_NOC_MISTYROSE2 = 341

    Quantity_NOC_MISTYROSE3 = 342

    Quantity_NOC_MISTYROSE4 = 343

    Quantity_NOC_MOCCASIN = 344

    Quantity_NOC_NAVAJOWHITE1 = 345

    Quantity_NOC_NAVAJOWHITE2 = 346

    Quantity_NOC_NAVAJOWHITE3 = 347

    Quantity_NOC_NAVAJOWHITE4 = 348

    Quantity_NOC_NAVYBLUE = 349

    Quantity_NOC_OLDLACE = 350

    Quantity_NOC_OLIVEDRAB = 351

    Quantity_NOC_OLIVEDRAB1 = 352

    Quantity_NOC_OLIVEDRAB2 = 353

    Quantity_NOC_OLIVEDRAB3 = 354

    Quantity_NOC_OLIVEDRAB4 = 355

    Quantity_NOC_ORANGE = 356

    Quantity_NOC_ORANGE1 = 356

    Quantity_NOC_ORANGE2 = 357

    Quantity_NOC_ORANGE3 = 358

    Quantity_NOC_ORANGE4 = 359

    Quantity_NOC_ORANGERED = 360

    Quantity_NOC_ORANGERED1 = 360

    Quantity_NOC_ORANGERED2 = 361

    Quantity_NOC_ORANGERED3 = 362

    Quantity_NOC_ORANGERED4 = 363

    Quantity_NOC_ORCHID = 364

    Quantity_NOC_ORCHID1 = 365

    Quantity_NOC_ORCHID2 = 366

    Quantity_NOC_ORCHID3 = 367

    Quantity_NOC_ORCHID4 = 368

    Quantity_NOC_PALEGOLDENROD = 369

    Quantity_NOC_PALEGREEN = 370

    Quantity_NOC_PALEGREEN1 = 371

    Quantity_NOC_PALEGREEN2 = 372

    Quantity_NOC_PALEGREEN3 = 373

    Quantity_NOC_PALEGREEN4 = 374

    Quantity_NOC_PALETURQUOISE = 375

    Quantity_NOC_PALETURQUOISE1 = 376

    Quantity_NOC_PALETURQUOISE2 = 377

    Quantity_NOC_PALETURQUOISE3 = 378

    Quantity_NOC_PALETURQUOISE4 = 379

    Quantity_NOC_PALEVIOLETRED = 380

    Quantity_NOC_PALEVIOLETRED1 = 381

    Quantity_NOC_PALEVIOLETRED2 = 382

    Quantity_NOC_PALEVIOLETRED3 = 383

    Quantity_NOC_PALEVIOLETRED4 = 384

    Quantity_NOC_PAPAYAWHIP = 385

    Quantity_NOC_PEACHPUFF = 386

    Quantity_NOC_PEACHPUFF2 = 387

    Quantity_NOC_PEACHPUFF3 = 388

    Quantity_NOC_PEACHPUFF4 = 389

    Quantity_NOC_PERU = 390

    Quantity_NOC_PINK = 391

    Quantity_NOC_PINK1 = 392

    Quantity_NOC_PINK2 = 393

    Quantity_NOC_PINK3 = 394

    Quantity_NOC_PINK4 = 395

    Quantity_NOC_PLUM = 396

    Quantity_NOC_PLUM1 = 397

    Quantity_NOC_PLUM2 = 398

    Quantity_NOC_PLUM3 = 399

    Quantity_NOC_PLUM4 = 400

    Quantity_NOC_POWDERBLUE = 401

    Quantity_NOC_PURPLE = 402

    Quantity_NOC_PURPLE1 = 403

    Quantity_NOC_PURPLE2 = 404

    Quantity_NOC_PURPLE3 = 405

    Quantity_NOC_PURPLE4 = 406

    Quantity_NOC_RED = 407

    Quantity_NOC_RED1 = 407

    Quantity_NOC_RED2 = 408

    Quantity_NOC_RED3 = 409

    Quantity_NOC_RED4 = 410

    Quantity_NOC_ROSYBROWN = 411

    Quantity_NOC_ROSYBROWN1 = 412

    Quantity_NOC_ROSYBROWN2 = 413

    Quantity_NOC_ROSYBROWN3 = 414

    Quantity_NOC_ROSYBROWN4 = 415

    Quantity_NOC_ROYALBLUE = 416

    Quantity_NOC_ROYALBLUE1 = 417

    Quantity_NOC_ROYALBLUE2 = 418

    Quantity_NOC_ROYALBLUE3 = 419

    Quantity_NOC_ROYALBLUE4 = 420

    Quantity_NOC_SADDLEBROWN = 421

    Quantity_NOC_SALMON = 422

    Quantity_NOC_SALMON1 = 423

    Quantity_NOC_SALMON2 = 424

    Quantity_NOC_SALMON3 = 425

    Quantity_NOC_SALMON4 = 426

    Quantity_NOC_SANDYBROWN = 427

    Quantity_NOC_SEAGREEN = 428

    Quantity_NOC_SEAGREEN1 = 429

    Quantity_NOC_SEAGREEN2 = 430

    Quantity_NOC_SEAGREEN3 = 431

    Quantity_NOC_SEAGREEN4 = 432

    Quantity_NOC_SEASHELL = 433

    Quantity_NOC_SEASHELL2 = 434

    Quantity_NOC_SEASHELL3 = 435

    Quantity_NOC_SEASHELL4 = 436

    Quantity_NOC_BEET = 437

    Quantity_NOC_TEAL = 438

    Quantity_NOC_SIENNA = 439

    Quantity_NOC_SIENNA1 = 440

    Quantity_NOC_SIENNA2 = 441

    Quantity_NOC_SIENNA3 = 442

    Quantity_NOC_SIENNA4 = 443

    Quantity_NOC_SKYBLUE = 444

    Quantity_NOC_SKYBLUE1 = 445

    Quantity_NOC_SKYBLUE2 = 446

    Quantity_NOC_SKYBLUE3 = 447

    Quantity_NOC_SKYBLUE4 = 448

    Quantity_NOC_SLATEBLUE = 449

    Quantity_NOC_SLATEBLUE1 = 450

    Quantity_NOC_SLATEBLUE2 = 451

    Quantity_NOC_SLATEBLUE3 = 452

    Quantity_NOC_SLATEBLUE4 = 453

    Quantity_NOC_SLATEGRAY1 = 454

    Quantity_NOC_SLATEGRAY2 = 455

    Quantity_NOC_SLATEGRAY3 = 456

    Quantity_NOC_SLATEGRAY4 = 457

    Quantity_NOC_SLATEGRAY = 458

    Quantity_NOC_SNOW = 459

    Quantity_NOC_SNOW2 = 460

    Quantity_NOC_SNOW3 = 461

    Quantity_NOC_SNOW4 = 462

    Quantity_NOC_SPRINGGREEN = 463

    Quantity_NOC_SPRINGGREEN2 = 464

    Quantity_NOC_SPRINGGREEN3 = 465

    Quantity_NOC_SPRINGGREEN4 = 466

    Quantity_NOC_STEELBLUE = 467

    Quantity_NOC_STEELBLUE1 = 468

    Quantity_NOC_STEELBLUE2 = 469

    Quantity_NOC_STEELBLUE3 = 470

    Quantity_NOC_STEELBLUE4 = 471

    Quantity_NOC_TAN = 472

    Quantity_NOC_TAN1 = 473

    Quantity_NOC_TAN2 = 474

    Quantity_NOC_TAN3 = 475

    Quantity_NOC_TAN4 = 476

    Quantity_NOC_THISTLE = 477

    Quantity_NOC_THISTLE1 = 478

    Quantity_NOC_THISTLE2 = 479

    Quantity_NOC_THISTLE3 = 480

    Quantity_NOC_THISTLE4 = 481

    Quantity_NOC_TOMATO = 482

    Quantity_NOC_TOMATO1 = 482

    Quantity_NOC_TOMATO2 = 483

    Quantity_NOC_TOMATO3 = 484

    Quantity_NOC_TOMATO4 = 485

    Quantity_NOC_TURQUOISE = 486

    Quantity_NOC_TURQUOISE1 = 487

    Quantity_NOC_TURQUOISE2 = 488

    Quantity_NOC_TURQUOISE3 = 489

    Quantity_NOC_TURQUOISE4 = 490

    Quantity_NOC_VIOLET = 491

    Quantity_NOC_VIOLETRED = 492

    Quantity_NOC_VIOLETRED1 = 493

    Quantity_NOC_VIOLETRED2 = 494

    Quantity_NOC_VIOLETRED3 = 495

    Quantity_NOC_VIOLETRED4 = 496

    Quantity_NOC_WHEAT = 497

    Quantity_NOC_WHEAT1 = 498

    Quantity_NOC_WHEAT2 = 499

    Quantity_NOC_WHEAT3 = 500

    Quantity_NOC_WHEAT4 = 501

    Quantity_NOC_WHITESMOKE = 502

    Quantity_NOC_YELLOW = 503

    Quantity_NOC_YELLOW1 = 503

    Quantity_NOC_YELLOW2 = 504

    Quantity_NOC_YELLOW3 = 505

    Quantity_NOC_YELLOW4 = 506

    Quantity_NOC_YELLOWGREEN = 507

    Quantity_NOC_WHITE = 508

class Quantity_TypeOfColor(enum.IntEnum):
    """Identifies color definition systems."""

    Quantity_TOC_RGB = 0

    Quantity_TOC_sRGB = 1

    Quantity_TOC_HLS = 2

    Quantity_TOC_CIELab = 3

    Quantity_TOC_CIELch = 4

class Quantity_Color:
    """
    This class allows the definition of an RGB color as triplet of 3 normalized floating point
    values (red, green, blue).

    Although Quantity_Color can be technically used for pass-through storage of RGB triplet in any
    color space, other OCCT interfaces taking/returning Quantity_Color would expect them in linear
    space. Therefore, take a look into methods converting to and from non-linear sRGB color space,
    if needed; for instance, application usually providing color picking within 0..255 range in sRGB
    color space.
    """

    @overload
    def __init__(self) -> None:
        """Creates Quantity_NOC_YELLOW color (for historical reasons)."""

    @overload
    def __init__(self, theName: Quantity_NameOfColor) -> None:
        """Creates the color from enumeration value."""

    @overload
    def __init__(self, theRgb: nanoocp.BVH.BVH_Vec3f) -> None:
        """Define color from linear RGB values."""

    @overload
    def __init__(self, theC1: float, theC2: float, theC3: float, theType: Quantity_TypeOfColor) -> None:
        """
        Creates a color according to the definition system theType.
        Throws exception if values are out of range.
        """

    def Name(self) -> Quantity_NameOfColor:
        """
        Returns the name of the nearest color from the Quantity_NameOfColor enumeration.
        """

    @overload
    def SetValues(self, theName: Quantity_NameOfColor) -> None:
        """Updates the color from specified named color."""

    @overload
    def SetValues(self, theC1: float, theC2: float, theC3: float, theType: Quantity_TypeOfColor) -> None:
        """
        Updates a color according to the mode specified by theType.
        Throws exception if values are out of range.
        """

    def Rgb(self) -> nanoocp.BVH.BVH_Vec3f:
        """Return the color as vector of 3 float elements."""

    def Values(self, theType: Quantity_TypeOfColor) -> tuple[float, float, float]:
        """
        Returns in theC1, theC2 and theC3 the components of this color
        according to the color system definition theType.
        """

    def Red(self) -> float:
        """
        Returns the Red component (quantity of red) of the color within range [0.0; 1.0].
        """

    def Green(self) -> float:
        """
        Returns the Green component (quantity of green) of the color within range [0.0; 1.0].
        """

    def Blue(self) -> float:
        """
        Returns the Blue component (quantity of blue) of the color within range [0.0; 1.0].
        """

    def Hue(self) -> float:
        """
        Returns the Hue component (hue angle) of the color
        in degrees within range [0.0; 360.0], 0.0 being Red.
        -1.0 is a special value reserved for grayscale color (S should be 0.0)
        """

    def Light(self) -> float:
        """
        Returns the Light component (value of the lightness) of the color within range [0.0; 1.0].
        """

    def ChangeIntensity(self, theDelta: float) -> None:
        """
        Increases or decreases the intensity (variation of the lightness).
        The delta is a percentage. Any value greater than zero will increase the intensity.
        The variation is expressed as a percentage of the current value.
        """

    def Saturation(self) -> float:
        """
        Returns the Saturation component (value of the saturation) of the color within range
        [0.0; 1.0].
        """

    def ChangeContrast(self, theDelta: float) -> None:
        """
        Increases or decreases the contrast (variation of the saturation).
        The delta is a percentage. Any value greater than zero will increase the contrast.
        The variation is expressed as a percentage of the current value.
        """

    def IsDifferent(self, theOther: Quantity_Color) -> bool:
        """
        Returns TRUE if the distance between two colors is greater than Epsilon().
        """

    def __ne__(self, theOther: Quantity_Color) -> bool:
        """Alias to IsDifferent()."""

    def IsEqual(self, theOther: Quantity_Color) -> bool:
        """
        Returns TRUE if the distance between two colors is no greater than Epsilon().
        """

    def __eq__(self, theOther: Quantity_Color) -> bool:
        """Alias to IsEqual()."""

    def Distance(self, theColor: Quantity_Color) -> float:
        """
        Returns the distance between two colors. It's a value between 0 and the square root of 3 (the
        black/white distance).
        """

    def SquareDistance(self, theColor: Quantity_Color) -> float:
        """Returns the square of distance between two colors."""

    def Delta(self, theColor: Quantity_Color) -> tuple[float, float]:
        """
        Returns the percentage change of contrast and intensity between this and another color.
        <DC> and <DI> are percentages, either positive or negative.
        The calculation is with respect to this color.
        If <DC> is positive then <me> is more contrasty.
        If <DI> is positive then <me> is more intense.
        """

    def DeltaE2000(self, theOther: Quantity_Color) -> float:
        """
        Returns the value of the perceptual difference between this color
        and @p theOther, computed using the CIEDE2000 formula.
        The difference is in range [0, 100.], with 1 approximately corresponding
        to the minimal perceivable difference (usually difference 5 or greater is
        needed for the difference to be recognizable in practice).
        """

    @staticmethod
    def Name_s(theR: float, theG: float, theB: float) -> Quantity_NameOfColor:
        """
        Returns the color from Quantity_NameOfColor enumeration nearest to specified RGB values.
        """

    @staticmethod
    def StringName(theColor: Quantity_NameOfColor) -> str:
        """
        Returns the name of the color identified by the given Quantity_NameOfColor enumeration value.
        """

    @overload
    @staticmethod
    def ColorFromName(theName: str) -> tuple[bool, Quantity_NameOfColor]:
        """
        Finds color from predefined names.
        For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK.
        Returns FALSE if name is unknown.
        """

    @overload
    @staticmethod
    def ColorFromName(theColorNameString: str, theColor: Quantity_Color) -> bool:
        """
        Finds color from predefined names.
        @param theColorNameString the color name
        @param theColor a found color
        @return false if the color name is unknown, or true if the search by color name was successful
        """

    @staticmethod
    def ColorFromHex(theHexColorString: str, theColor: Quantity_Color) -> bool:
        """
        Parses the string as a hex color (like "#FF0" for short sRGB color, or "#FFFF00" for sRGB
        color)
        @param theHexColorString the string to be parsed
        @param theColor a color that is a result of parsing
        @return true if parsing was successful, or false otherwise
        """

    @staticmethod
    def ColorToHex(theColor: Quantity_Color, theToPrefixHash: bool = True) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns hex sRGB string in format "#FFAAFF"."""

    @staticmethod
    def Convert_sRGB_To_HLS(theRgb: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts sRGB components into HLS ones."""

    @staticmethod
    def Convert_HLS_To_sRGB(theHls: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts HLS components into RGB ones."""

    @staticmethod
    def Convert_LinearRGB_To_HLS(theRgb: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts Linear RGB components into HLS ones."""

    @staticmethod
    def Convert_HLS_To_LinearRGB(theHls: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts HLS components into linear RGB ones."""

    @staticmethod
    def Convert_LinearRGB_To_Lab(theRgb: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts linear RGB components into CIE Lab ones."""

    @staticmethod
    def Convert_Lab_To_Lch(theLab: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts CIE Lab components into CIE Lch ones."""

    @staticmethod
    def Convert_Lab_To_LinearRGB(theLab: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """
        Converts CIE Lab components into linear RGB ones.
        Note that the resulting values may be out of the valid range for RGB.
        """

    @staticmethod
    def Convert_Lch_To_Lab(theLch: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """Converts CIE Lch components into CIE Lab ones."""

    @staticmethod
    def Color2argb(theColor: Quantity_Color) -> int:
        """
        Convert the color value to ARGB integer value, with alpha equals to 0.
        So the output is formatted as 0x00RRGGBB.
        Note that this unpacking does NOT involve non-linear sRGB -> linear RGB conversion,
        as would be usually expected for RGB color packed into 4 bytes.
        @param[in] theColor  color to convert
        @param[out] theARGB  result color encoded as integer
        """

    @staticmethod
    def Argb2color(theARGB: int, theColor: Quantity_Color) -> None:
        """
        Convert integer ARGB value to Color. Alpha bits are ignored.
        Note that this packing does NOT involve linear -> non-linear sRGB conversion,
        as would be usually expected to preserve higher (for human eye) color precision in 4 bytes.
        """

    @overload
    @staticmethod
    def Convert_LinearRGB_To_sRGB(theLinearValue: float) -> float:
        """
        Convert linear RGB component into sRGB using OpenGL specs formula (double precision), also
        known as gamma correction.
        """

    @overload
    @staticmethod
    def Convert_LinearRGB_To_sRGB(theLinearValue: float) -> float:
        """
        Convert linear RGB component into sRGB using OpenGL specs formula (single precision), also
        known as gamma correction.
        """

    @overload
    @staticmethod
    def Convert_sRGB_To_LinearRGB(thesRGBValue: float) -> float:
        """
        Convert sRGB component into linear RGB using OpenGL specs formula (double precision), also
        known as gamma correction.
        """

    @overload
    @staticmethod
    def Convert_sRGB_To_LinearRGB(thesRGBValue: float) -> float:
        """
        Convert sRGB component into linear RGB using OpenGL specs formula (single precision), also
        known as gamma correction.
        """

    @overload
    @staticmethod
    def Convert_LinearRGB_To_sRGB_approx22(theLinearValue: float) -> float:
        """
        Convert linear RGB component into sRGB using approximated uniform gamma coefficient 2.2.
        """

    @overload
    @staticmethod
    def Convert_LinearRGB_To_sRGB_approx22(theRGB: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """
        Convert linear RGB components into sRGB using approximated uniform gamma coefficient 2.2
        """

    @overload
    @staticmethod
    def Convert_sRGB_To_LinearRGB_approx22(thesRGBValue: float) -> float:
        """
        Convert sRGB component into linear RGB using approximated uniform gamma coefficient 2.2
        """

    @overload
    @staticmethod
    def Convert_sRGB_To_LinearRGB_approx22(theRGB: nanoocp.BVH.BVH_Vec3f) -> nanoocp.BVH.BVH_Vec3f:
        """
        Convert sRGB components into linear RGB using approximated uniform gamma coefficient 2.2
        """

    @staticmethod
    def HlsRgb(theH: float, theL: float, theS: float) -> tuple[float, float, float]:
        """Converts HLS components into sRGB ones."""

    @staticmethod
    def RgbHls(theR: float, theG: float, theB: float) -> tuple[float, float, float]:
        """Converts sRGB components into HLS ones."""

    @staticmethod
    def Epsilon() -> float:
        """
        Returns the value used to compare two colors for equality; 0.0001 by default.
        """

    @staticmethod
    def SetEpsilon(theEpsilon: float) -> None:
        """Set the value used to compare two colors for equality."""

class Quantity_ColorRGBA:
    """
    The pair of Quantity_Color and Alpha component (1.0 opaque, 0.0 transparent).
    """

    @overload
    def __init__(self) -> None:
        """Creates a color with the default value."""

    @overload
    def __init__(self, theRgb: Quantity_Color) -> None:
        """Creates the color with specified RGB value."""

    @overload
    def __init__(self, theRgba: nanoocp.BVH.BVH_Vec4f) -> None:
        """Creates the color from RGBA vector."""

    @overload
    def __init__(self, theRgb: Quantity_Color, theAlpha: float) -> None:
        """Creates the color with specified RGBA values."""

    @overload
    def __init__(self, theRed: float, theGreen: float, theBlue: float, theAlpha: float) -> None:
        """Creates the color from RGBA values."""

    def SetValues(self, theRed: float, theGreen: float, theBlue: float, theAlpha: float) -> None:
        """Assign new values to the color."""

    def GetRGB(self) -> Quantity_Color:
        """Return RGB color value."""

    def ChangeRGB(self) -> Quantity_Color:
        """Modify RGB color components without affecting alpha value."""

    def SetRGB(self, theRgb: Quantity_Color) -> None:
        """Assign RGB color components without affecting alpha value."""

    def Alpha(self) -> float:
        """Return alpha value (1.0 means opaque, 0.0 means fully transparent)."""

    def SetAlpha(self, theAlpha: float) -> None:
        """Assign the alpha value."""

    def IsDifferent(self, theOther: Quantity_ColorRGBA) -> bool:
        """Returns true if the distance between colors is greater than Epsilon()."""

    def __ne__(self, theOther: Quantity_ColorRGBA) -> bool:
        """Returns true if the distance between colors is greater than Epsilon()."""

    def IsEqual(self, theOther: Quantity_ColorRGBA) -> bool:
        """
        Two colors are considered to be equal if their distance is no greater than Epsilon().
        """

    def __eq__(self, theOther: Quantity_ColorRGBA) -> bool:
        """
        Two colors are considered to be equal if their distance is no greater than Epsilon().
        """

    @staticmethod
    def ColorFromName(theColorNameString: str, theColor: Quantity_ColorRGBA) -> bool:
        """
        Finds color from predefined names.
        For example, the name of the color which corresponds to "BLACK" is Quantity_NOC_BLACK.
        An alpha component is set to 1.0.
        @param theColorNameString the color name
        @param theColor a found color
        @return false if the color name is unknown, or true if the search by color name was successful
        """

    @staticmethod
    def ColorFromHex(theHexColorString: str, theColor: Quantity_ColorRGBA, theAlphaComponentIsOff: bool = False) -> bool:
        """
        Parses the string as a hex color (like "#FF0" for short sRGB color, "#FF0F" for short sRGBA
        color,
        "#FFFF00" for RGB color, or "#FFFF00FF" for RGBA color)
        @param theHexColorString the string to be parsed
        @param theColor a color that is a result of parsing
        @param theAlphaComponentIsOff the flag that indicates if a color alpha component is presented
        in the input string (false) or not (true)
        @return true if parsing was successful, or false otherwise
        """

    @staticmethod
    def ColorToHex(theColor: Quantity_ColorRGBA, theToPrefixHash: bool = True) -> nanoocp.TCollection.TCollection_AsciiString:
        """Returns hex sRGBA string in format "#RRGGBBAA"."""

    @staticmethod
    def Convert_LinearRGB_To_sRGB(theRGB: nanoocp.BVH.BVH_Vec4f) -> nanoocp.BVH.BVH_Vec4f:
        """Convert linear RGB components into sRGB using OpenGL specs formula."""

    @staticmethod
    def Convert_sRGB_To_LinearRGB(theRGB: nanoocp.BVH.BVH_Vec4f) -> nanoocp.BVH.BVH_Vec4f:
        """Convert sRGB components into linear RGB using OpenGL specs formula."""

class Quantity_Date:
    """
    This class provides services to manage date information.
    A date represents the following time intervals:
    year, month, day, hour, minute, second,
    millisecond and microsecond.
    Current time is expressed in elapsed seconds
    and microseconds beginning from 00:00 GMT,
    January 1, 1979 (zero hour). The valid date can
    only be later than this one.
    Note: a Period object gives the interval between two dates.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a default date
        (00:00 GMT, January 1, 1979 (zero hour)); use the function
        SetValues to define the required date; or
        """

    @overload
    def __init__(self, mm: int, dd: int, yyyy: int, hh: int, mn: int, ss: int, mis: int = 0, mics: int = 0) -> None:
        """
        Constructs a date from the year yyyy, the
        month mm, the day dd, the hour hh, the minute
        mn, the second ss, the millisecond mis
        (defaulted to 0) and the microsecond mics (defaulted to 0).
        With:
        1 <= mm <= 12
        1 <= dd <= max number of days of <mm>
        1979 <= yyyy
        0 <= hh <= 23
        0 <= mn <= 59
        0 <= ss <= 59
        0 <= mis <= 999
        0 <= mics <= 999
        Exceptions
        Quantity_DateDefinitionError if mm, dd, hh,
        mn, ss, mis and mics are not the components of the valid date.
        """

    def Values(self) -> tuple[int, int, int, int, int, int, int, int]:
        """
        Gets a complete Date.
        -   in mm - the month,
        -   in dd - the day,
        -   in yyyy - the year,
        -   in hh - the hour,
        -   in mn - the minute,
        -   in ss - the second,
        -   in mis - the millisecond, and
        -   in mics - the microsecond
        """

    def SetValues(self, mm: int, dd: int, yy: int, hh: int, mn: int, ss: int, mis: int = 0, mics: int = 0) -> None:
        """
        Assigns to this date the year yyyy, the month
        mm, the day dd, the hour hh, the minute mn, the
        second ss, the millisecond mis (defaulted to 0)
        and the microsecond mics (defaulted to 0).
        Exceptions
        Quantity_DateDefinitionError if mm, dd, hh,
        mn, ss, mis and mics are not components of a valid date.
        """

    def Difference(self, anOther: Quantity_Date) -> Quantity_Period:
        """
        Subtracts one Date from another one to find the period
        between and returns the value.
        The result is the absolute value between the difference
        of two dates.
        """

    def Subtract(self, aPeriod: Quantity_Period) -> Quantity_Date:
        """
        Subtracts a period from a Date and returns the new Date.
        Raises an exception if the result date is anterior to
        Jan 1, 1979.
        """

    def __sub__(self, aPeriod: Quantity_Period) -> Quantity_Date: ...

    def Add(self, aPeriod: Quantity_Period) -> Quantity_Date:
        """Adds a Period to a Date and returns the new Date."""

    def __add__(self, aPeriod: Quantity_Period) -> Quantity_Date: ...

    def Year(self) -> int:
        """Returns year of a Date."""

    def Month(self) -> int:
        """Returns month of a Date."""

    def Day(self) -> int:
        """Returns Day of a Date."""

    def Hour(self) -> int:
        """Returns Hour of a Date."""

    def Minute(self) -> int:
        """Returns minute of a Date."""

    def Second(self) -> int:
        """Returns second of a Date."""

    def MilliSecond(self) -> int:
        """Returns millisecond of a Date."""

    def MicroSecond(self) -> int:
        """Returns microsecond of a Date."""

    def IsEqual(self, anOther: Quantity_Date) -> bool:
        """
        Returns TRUE if both <me> and <other> are equal.
        This method is an alias of operator ==.
        """

    def __eq__(self, anOther: Quantity_Date) -> bool: ...

    def IsEarlier(self, anOther: Quantity_Date) -> bool:
        """Returns TRUE if <me> is earlier than <other>."""

    def __lt__(self, anOther: Quantity_Date) -> bool: ...

    def IsLater(self, anOther: Quantity_Date) -> bool:
        """Returns TRUE if <me> is later then <other>."""

    def __gt__(self, anOther: Quantity_Date) -> bool: ...

    @staticmethod
    def IsValid(mm: int, dd: int, yy: int, hh: int, mn: int, ss: int, mis: int = 0, mics: int = 0) -> bool:
        """
        Checks the validity of a date - returns true if a
        date defined from the year yyyy, the month mm,
        the day dd, the hour hh, the minute mn, the
        second ss, the millisecond mis (defaulted to 0)
        and the microsecond mics (defaulted to 0) is valid.
        A date must satisfy the conditions above:
        -   yyyy is greater than or equal to 1979,
        -   mm lies within the range [1, 12] (with 1
        corresponding to January and 12 to December),
        -   dd lies within a valid range for the month mm
        (from 1 to 28, 29, 30 or 31 depending on
        mm and whether yyyy is a leap year or not),
        -   hh lies within the range [0, 23],
        -   mn lies within the range [0, 59],
        -   ss lies within the range [0, 59],
        -   mis lies within the range [0, 999],
        -   mics lies within the range [0, 999].C
        """

    @staticmethod
    def IsLeap(yy: int) -> bool:
        """
        Returns true if a year is a leap year.
        The leap years are divisible by 4 and not by 100 except
        the years divisible by 400.
        """

class Quantity_DateDefinitionError(nanoocp.Standard.Standard_DomainError):
    pass

class Quantity_Period:
    """
    Manages date intervals. For example, a Period object
    gives the interval between two dates.
    A period is expressed in seconds and microseconds.
    """

    @overload
    def __init__(self, ss: int, mics: int = 0) -> None:
        """
        Creates a Period with a number of seconds and microseconds.
        Exceptions
        Quantity_PeriodDefinitionError:
        -   if the number of seconds expressed either by:
        -   dd days, hh hours, mn minutes and ss seconds, or
        -   Ss
        is less than 0.
        -   if the number of microseconds expressed either by:
        -   mis milliseconds and mics microseconds, or
        -   Mics
        is less than 0.
        """

    @overload
    def __init__(self, dd: int, hh: int, mn: int, ss: int, mis: int = 0, mics: int = 0) -> None:
        """
        Creates a Period
        With:
        0 <= dd
        0 <= hh
        0 <= mn
        0 <= ss
        0 <= mis
        0 <= mics
        """

    @overload
    def Values(self) -> tuple[int, int, int, int, int, int]:
        """
        Decomposes this period into a number of days,hours,
        minutes,seconds,milliseconds and microseconds
        Example of return values:
        2 days, 15 hours, 0 minute , 0 second
        0 millisecond and 0 microsecond
        """

    @overload
    def Values(self) -> tuple[int, int]:
        """
        Returns the number of seconds in Ss and the
        number of remainding microseconds in Mics of this period.
        Example of return values: 3600 seconds and 0 microseconds
        """

    @overload
    def SetValues(self, dd: int, hh: int, mn: int, ss: int, mis: int = 0, mics: int = 0) -> None:
        """
        Assigns to this period the time interval defined
        -   with dd days, hh hours, mn minutes, ss
        seconds, mis (defaulted to 0) milliseconds and
        mics (defaulted to 0) microseconds; or
        """

    @overload
    def SetValues(self, ss: int, mics: int = 0) -> None:
        """
        Assigns to this period the time interval defined
        -   with Ss seconds and Mics (defaulted to 0) microseconds.
        Exceptions
        Quantity_PeriodDefinitionError:
        -   if the number of seconds expressed either by:
        -   dd days, hh hours, mn minutes and ss seconds, or
        -   Ss
        is less than 0.
        -   if the number of microseconds expressed either by:
        -   mis milliseconds and mics microseconds, or
        -   Mics
        is less than 0.
        """

    def Subtract(self, anOther: Quantity_Period) -> Quantity_Period:
        """Subtracts one Period from another and returns the difference."""

    def __sub__(self, anOther: Quantity_Period) -> Quantity_Period: ...

    def Add(self, anOther: Quantity_Period) -> Quantity_Period:
        """Adds one Period to another one."""

    def __add__(self, anOther: Quantity_Period) -> Quantity_Period: ...

    def IsEqual(self, anOther: Quantity_Period) -> bool:
        """Returns TRUE if both <me> and <other> are equal."""

    def __eq__(self, anOther: Quantity_Period) -> bool: ...

    def IsShorter(self, anOther: Quantity_Period) -> bool:
        """Returns TRUE if <me> is shorter than <other>."""

    def __lt__(self, anOther: Quantity_Period) -> bool: ...

    def IsLonger(self, anOther: Quantity_Period) -> bool:
        """Returns TRUE if <me> is longer then <other>."""

    def __gt__(self, anOther: Quantity_Period) -> bool: ...

    @overload
    @staticmethod
    def IsValid(dd: int, hh: int, mn: int, ss: int, mis: int = 0, mics: int = 0) -> bool:
        """
        Checks the validity of a Period in form (dd,hh,mn,ss,mil,mic)
        With:
        0 <= dd
        0 <= hh
        0 <= mn
        0 <= ss
        0 <= mis
        0 <= mics
        """

    @overload
    @staticmethod
    def IsValid(ss: int, mics: int = 0) -> bool:
        """
        Checks the validity of a Period in form (ss,mic)
        With:
        0 <= ss
        0 <= mics
        """

class Quantity_PeriodDefinitionError(nanoocp.Standard.Standard_DomainError):
    pass
