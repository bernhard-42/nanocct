// R-OWNER (Binding-Rules.md): who owns an OCAF object, for nanocct::owners (nanocct_lifetime.h). Included by the generated files
// that apply the rule -- the toolkits that link TKLCAF -- and nowhere else.
#pragma once

#include "nanocct_common.h"

#include <TDF_Attribute.hxx>
#include <TDF_Data.hxx>
#include <TDF_Label.hxx>
#include <TDocStd_Document.hxx>
#include <TDocStd_Owner.hxx>

namespace nanocct {
struct ocaf_owners {
    // A document's data carries a TDocStd_Owner on its root, which points at the document (a raw pointer: the document
    // itself has no destructor that would clear it). Kept: the document, so that TDocStd_Document::Get(label) and every
    // other way back from the data to its document stay valid.
    static void data(PyObject *nurse, const TDF_Data &d) {
        opencascade::handle<TDocStd_Owner> owner;
        if (d.Root().FindAttribute(TDocStd_Owner::GetID(), owner)) {
            opencascade::handle<TDocStd_Document> document = owner->GetDocument();
            if (!document.IsNull())
                nb::keep_alive_obj(nurse, nb::cast(document));
        }
    }
    // A label points at a node of its data's tree: kept, the data and the data's document. A null label has neither.
    static void label(PyObject *nurse, const TDF_Label &l) {
        if (l.IsNull())
            return;
        opencascade::handle<TDF_Data> d = l.Data();
        if (d.IsNull())
            return;
        nb::keep_alive_obj(nurse, nb::cast(d));
        data(nurse, *d);
    }
    static void transient(PyObject *nurse, const TDF_Data &d) { data(nurse, d); }
    // An attribute points at the node of its label (none while it is not attached).
    static void transient(PyObject *nurse, const TDF_Attribute &a) { label(nurse, a.Label()); }
};
} // namespace nanocct
